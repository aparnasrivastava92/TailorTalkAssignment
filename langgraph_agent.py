from backend.google_calendar import check_availability, book_slot
from datetime import datetime, timedelta

def chat_with_agent(message: str) -> str:
    message = message.lower()
    if "availability" in message or "free" in message:
        return check_availability()
    elif "schedule" in message or "book" in message:
        now = datetime.utcnow() + timedelta(days=1)
        start_time = now.replace(hour=14, minute=0, second=0, microsecond=0).isoformat()
        end_time = (now + timedelta(hours=1)).replace(hour=15, minute=0, second=0, microsecond=0).isoformat()
        return book_slot(start_time=start_time, end_time=end_time)
    return "Please specify if you want to check availability or book a meeting."
