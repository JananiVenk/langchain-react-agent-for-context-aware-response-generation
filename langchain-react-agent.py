from langchain_community.tools import WikipediaQueryRun  # pip install wikipedia
from langchain_community.utilities import WikipediaAPIWrapper,GoogleSerperAPIWrapper
from langchain_community.tools import YouTubeSearchTool
from openai import OpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain.agents import Tool


wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wikipedia = WikipediaQueryRun(description="A tool to explain things in text format. Use this tool if you think the user’s asked concept is best explained through text.", api_wrapper=wiki_api_wrapper)


youtube = YouTubeSearchTool(
   description="A tool to search YouTube videos. Use this tool if you think the user’s asked concept can be best explained by watching a video."
)

search = GoogleSerperAPIWrapper(serper_api_key="your_serper_key")
serper=Tool(
        name="serper_tool",
        func=search.run,
        description="use when text and video links doesn't best suit the user's query."
    )

tools = [wikipedia, youtube,serper]
llm = ChatOpenAI(
    model="gpt-4o",
    api_key="your_openai_key"
)

system_prompt = SystemMessage(
   """
   You are a helpful bot named Chandler. Your task is to explain topics
   asked by the user via two mediums: text or video link or link.
  
   If the asked topic is best explained in text format, use the Wikipedia tool.
   If video is the best medium to explain the topic, conduct a YouTube search on it
   and return found video links.
   Finally, if text and video links don't solve the user's query properly, use serper tool.

   """
)
agent = create_react_agent(llm, tools, state_modifier=system_prompt)
def execute(agent, query):
    print("Human Query:",query)
    response = agent.invoke({'messages': [HumanMessage(query)]})
    print("Tool used:",response['messages'][1].additional_kwargs['tool_calls'][0]['function']['name'])
    print("Result:")
    print(response['messages'][-1].content)
    print()

execute(agent,query="Explain AI")
execute(agent,query="Give me list of course links to learn AI")
execute(agent,query="Give some video tutorials for AI")