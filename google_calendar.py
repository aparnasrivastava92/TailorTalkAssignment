from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials/credentials.json'
CALENDAR_ID = 'your_calendar@gmail.com'  # Replace with your calendar ID

def get_calendar_service():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('calendar', 'v3', credentials=creds)

def check_availability():
    service = get_calendar_service()
    now = datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=now,
        maxResults=5,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])
    if not events:
        return "You're free for the next few hours."
    return f"Next event: {events[0]['summary']} at {events[0]['start'].get('dateTime')}"

def book_slot(summary="TailorTalk Appointment", start_time=None, end_time=None):
    service = get_calendar_service()
    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end_time, 'timeZone': 'Asia/Kolkata'},
    }
    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    return f"Event created: {event.get('htmlLink')}"
