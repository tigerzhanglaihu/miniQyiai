
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from tools.product_api_tool import ProductSearchTool

def create_sales_agent():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    tool = ProductSearchTool()
    tools = [Tool(name=tool.name, func=tool._run, description=tool.description)]
    return initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)
