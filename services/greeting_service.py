from datetime import datetime
from entities.greeting import Greeting

GREETINGS = {
    "fr": Greeting("Bonjour", "Bonsoir"),
    "en": Greeting("Good morning", "Good evening"),
    "es": Greeting("Buenos días", "Buenas noches"),
    "de": Greeting("Guten Morgen", "Guten Abend"),
}

def get_greeting(lang: str) -> str | None:
    greeting = GREETINGS.get(lang)
    if not greeting:
        return None
    hour = datetime.now().hour
    return greeting.evening if hour >= 18 else greeting.day
