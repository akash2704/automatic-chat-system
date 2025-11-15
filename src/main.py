
from fastapi import FastAPI

# We use relative imports to access our other modules
from .domain import ChatMessage, ChatReply
from .application import handle_chat_message

# Initialize FastAPI app
app = FastAPI(
    title="Mini Chat System (Refactored)",
    description="A simple intent-based chat system using Clean Architecture.",
)

@app.post("/chat", response_model=ChatReply)
def chat(user_message: ChatMessage):
    """
    The main chat endpoint.
    
    Accepts a user message, detects the intent, and returns an auto-reply.
    """
    # 1. Get the raw text from the domain model
    message_text = user_message.message
    
    # 2. Call our application logic
    reply_text = handle_chat_message(message_text)
    
    # 3. Return the response in the correct domain model
    return ChatReply(reply=reply_text)

@app.get("/")
def read_root():
    """
    A simple root endpoint to show the API is running.
    """
    return {"status": "Mini Chat System is running. Go to /docs to test."}
