from fastapi import FastAPI, Request
from backend.google_calendar import check_availability, book_slot
from agent.langgraph_agent import chat_with_agent

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")
    response = chat_with_agent(user_message)
    return {"response": response}
