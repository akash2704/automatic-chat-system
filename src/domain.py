# The domain layer holds the core data models.
# These models define the shape of data inside the system.
# I intentionally kept this layer free of any logic so it's clean and reusable.

from pydantic import BaseModel

class ChatMessage(BaseModel):
    # This model represents the incoming message from the user.
    # I’m validating it here so the rest of the system can assume it's always correct.
    message: str

class ChatReply(BaseModel):
    # This model wraps the response text.
    # Using a model instead of plain dicts keeps the API consistent and easy to document.
    reply: str
