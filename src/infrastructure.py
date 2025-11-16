# This file contains the static data that powers the system.
# I separated this from the application logic because it keeps things easier to update
# and makes the architecture more modular.

import re

# Here I'm defining a very simple intent-pattern system using regex.
# Regex gives me flexibility, and keeping them in a dict makes it easy to expand.
INTENT_PATTERNS = {
    "greeting": re.compile(r"\b(hi|hello|hey)\b", re.IGNORECASE),
    "farewell": re.compile(r"\b(bye|goodbye|see you)\b", re.IGNORECASE),
    "thanks": re.compile(r"\b(thank you|thanks)\b", re.IGNORECASE),
}

# These are the canned responses for each detected intent.
# I put them in a dictionary so the mapping stays readable and data-driven.
INTENT_RESPONSES = {
    "greeting": "Hello! How can I help you today?",
    "farewell": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "unknown": "I'm not sure I understand, but I'm learning!",
}
