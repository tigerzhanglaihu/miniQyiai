
import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent

def create_order_agent():
    base_url = os.getenv("OPENAPI_BASE_URL", "https://api.chatanywhere.tech/v1")
    openapi_spec = f"{base_url}/openapi.json"
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    '''
    toolkit = OpenAPIToolkit.from_url(openapi_spec)
    tools = toolkit.get_tools()
    return initialize_agent(tools, llm, agent_type="openapi-multi-tool", verbose=True)
    '''
    return "这是order agent！"
