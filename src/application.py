# This is the heart of the system.
# This layer contains the main logic that connects user input to the correct response.
# I intentionally kept this separated from the API and data layer to follow Clean Architecture.

from .infrastructure import INTENT_PATTERNS, INTENT_RESPONSES

def detect_intent(message: str) -> str:
    """
    Goes through all patterns and tries to match the user's message.

    I wanted this function to be very small and easy to read.
    By iterating over INTENT_PATTERNS, I can add more intents later without changing code.
    """
    for intent, pattern in INTENT_PATTERNS.items():
        if pattern.search(message):
            return intent

    # If no pattern matched, I fall back to 'unknown'
    return "unknown"

def get_reply(intent: str) -> str:
    """
    Returns a reply for the given intent.
    I use .get() with a default so the system never crashes even if an unknown intent appears.
    """
    return INTENT_RESPONSES.get(intent, INTENT_RESPONSES["unknown"])

def handle_chat_message(message: str) -> str:
    """
    This is the main service function that the API calls.

    I wrote it this way so the entire flow stays predictable:
    1. Detect intent
    2. Fetch the reply
    3. Return the reply text
    """

    # Step 1: Understand what the user is trying to say
    intent = detect_intent(message)

    # Step 2: Map that intent to a canned response
    reply = get_reply(intent)

    # Step 3: Return the final reply text
    return reply
