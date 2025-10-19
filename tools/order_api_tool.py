
import requests
from langchain.tools import BaseTool

class OrderStatusTool(BaseTool):
    name = "order_status"
    description = "查询用户订单状态"

    def _run(self, order_id: str):
        url = f"https://api.chatanywhere.tech/v1/orders/{order_id}"
        try:
            resp = requests.get(url, timeout=10)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
