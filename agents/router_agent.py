from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableSequence

"""1. 配置所有参数"""
# API配置
api_key =  "sk-IsaJkydPhYtOSR9Qh5aAkYz6Trnh3ow2h7RyAQa950JqmeEn"
base_url = "https://api.chatanywhere.tech/v1"
llm_model = "gpt-3.5-turbo"
temperature = 0

"""2. 定义 prompt"""
prompt = ChatPromptTemplate.from_template("""
你是一个电商客服AI，请从以下三个意图中选择一个：
1. 产品功能咨询（product_info）
2. 产品销售聊天（sales_chat）
3. 产品订单问题（order_service）

用户输入: {user_input}

请输出严格的 JSON，格式如下：
{{"intent": "...", "confidence": 0.0}}
""")

"""3. 初始化 LLM"""
llm = ChatOpenAI(
    api_key=api_key,
    base_url=base_url,
    model=llm_model,
    temperature=temperature,
)

"""4. 定义 JSON 输出解析器"""
parser = JsonOutputParser()

"""5. 组合为可运行链"""
router_agent = RunnableSequence(prompt | llm | parser)

"""6. 测试运行"""
if __name__ == "__main__":
    result = router_agent.invoke({"user_input": "我想退换货"})
    print(result)
