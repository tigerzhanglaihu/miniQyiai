from fastapi import FastAPI, Body
from pydantic import BaseModel
from dotenv import load_dotenv
import json
from agents.router_agent import router_agent
from agents.knowledge_agent import create_knowledge_agent
from agents.sales_agent import create_sales_agent
from agents.order_agent import create_order_agent

load_dotenv()

app = FastAPI(title="E-commerce Customer Service AI")

knowledge_agent = create_knowledge_agent()
sales_agent = create_sales_agent()
order_agent = create_order_agent()

class ChatRequest(BaseModel):
    user_input: str

@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    user_input = request.user_input
    route = router_agent.invoke({"user_input": user_input})
    try:
        route_json = json.loads(route)
    except Exception:
        return {"reply": "抱歉，我无法识别您的问题类型。", "intent": None}

    intent = route_json.get("intent", "")
    if intent == "product_info":
        result = knowledge_agent.run(user_input)
    elif intent == "sales_chat":
        result = sales_agent.run(user_input)
    elif intent == "order_service":
        result = order_agent.run(user_input)
    else:
        result = "抱歉，我不太明白您的需求。"

    return {"reply": result, "intent": intent}
