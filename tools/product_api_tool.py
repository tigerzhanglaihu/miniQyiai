
import requests
from langchain.tools import BaseTool

class ProductSearchTool(BaseTool):
    name = "product_search"
    description = "根据用户需求搜索推荐商品"

    def _run(self, query: str):
        url = "https://api.chatanywhere.tech/v1/products/search"
        try:
            resp = requests.get(url, params={"q": query}, timeout=10)
            return resp.json()
        except Exception as e:
            return {"error": str(e)}
