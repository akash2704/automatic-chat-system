from .infrastructure import INTENT_PATTERNS, INTENT_RESPONSES

def detect_intent(message: str) -> str:
    """
    Parses the user message to find the first matching intent.
    This is our "Intent/Key-Phrase Extractor".
    """
    for intent, pattern in INTENT_PATTERNS.items():
        if pattern.search(message):
            return intent
    
    # If no pattern matches, return the fallback intent
    return "fallback"

def get_reply(intent: str) -> str:
    """
    Retrieves the auto-reply for a given intent.
    This is our "Auto-Reply Generator".
    """
    return INTENT_RESPONSES.get(intent, INTENT_RESPONSES["fallback"])

# This is our main application service function
def handle_chat_message(message: str) -> str:
    """
    Orchestrates the chat logic:
    1. Detect intent from message
    2. Get auto-reply based on intent
    """
    intent = detect_intent(message)
    reply = get_reply(intent)
    return reply