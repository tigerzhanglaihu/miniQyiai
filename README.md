
# Customer Service AI (LangChain + FastAPI)

### Modules
- Router Agent: Detects intent
- Knowledge Agent: Handles product Q&A (PDF, DOCX, URLs)
- Sales Agent: Product recommendation
- Order Agent: OpenAPI integration for order service

### Run
```bash
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
