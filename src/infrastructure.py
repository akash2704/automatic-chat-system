import re

# We use regex patterns for simple key-phrase matching.
# The key is the "intent".
INTENT_PATTERNS = {
    "greeting": re.compile(r"\b(hi|hello|hey|yo)\b", re.IGNORECASE),
    "goodbye": re.compile(r"\b(bye|goodbye|see ya|cya)\b", re.IGNORECASE),
    "help": re.compile(r"\b(help|support|assist)\b", re.IGNORECASE),
    "order_status": re.compile(r"\b(order|status|where is my)\b", re.IGNORECASE),
    "thanks": re.compile(r"\b(thanks|thank you|thx)\b", re.IGNORECASE),
}

# This maps the detected intent to a response.
# This is our "Tables/Entities/Relationships" in its simplest form.
INTENT_RESPONSES = {
    "greeting": "Hello! How can I help you today?",
    "goodbye": "Goodbye! Have a great day.",
    "help": "I can help with order status or general questions. What do you need?",
    "order_status": "To check your order status, please provide your order number.",
    "thanks": "You're welcome!",
    "fallback": "I'm sorry, I don't understand that. Can you rephrase?",
}