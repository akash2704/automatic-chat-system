from pydantic import BaseModel
class ChatMessage(BaseModel):
    """
    Pydantic model for the incoming user message.
    FastAPI uses this to validate the request body.
    """
    message: str

class ChatReply(BaseModel):
    """
    Pydantic model for the outgoing chat reply.
    FastAPI uses this to serialize the response.
    """
    reply: str