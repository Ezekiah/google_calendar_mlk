from google.oauth2 import service_account
import googleapiclient.discovery
import datetime


SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin', 'https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'secret.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)


now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
print('Getting the upcoming 10 events')
eventsResult = service.events().list(
    calendarId='alexandreaazzouz@gmail.com', timeMin=now, maxResults=10, singleEvents=True,
    orderBy='startTime').execute()
events = eventsResult.get('items', [])

if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])

