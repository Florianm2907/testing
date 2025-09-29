asdf = []

from ics import Calendar
from datetime import datetime
from dateutil.rrule import rrulestr
import re

def convert_until_to_utc(until_str):
    # Parse UNTIL value from RRULE string
    until_dt = datetime.strptime(until_str, '%Y%m%dT%H%M%SZ')
    
    # Convert to UTC if not already
    if until_dt.tzinfo is not None:
        until_dt = until_dt.astimezone(datetime.timezone.utc)
    
    return until_dt

def list_events(ics_file):
    with open(ics_file, 'r', encoding='utf-8') as f:
        c = Calendar(f.read())
    
    for event in c.events:
        # Check if 'RRULE' exists in event's extra attributes
        if isinstance(event.extra, dict) and 'RRULE' in event.extra:
            rule = event.extra['RRULE']
            
            # Parse UNTIL value and convert to UTC
            until_match = re.search(r'UNTIL=(\d{8}T\d{6}Z)', rule)
            if until_match:
                until_str = until_match.group(1)
                until_dt = convert_until_to_utc(until_str)
                rule = rule.replace(until_str, until_dt.strftime('%Y%m%dT%H%M%SZ'))
            
            occurrences = rrulestr(rule, dtstart=event.begin.datetime)
            for occurrence in occurrences:
                # Calculate end time based on duration or difference between start and end times
                if event.duration:
                    end_time = occurrence + event.duration
                else:
                    end_time = occurrence + (event.end - event.begin)
                
                if not "Geburtstag" and not "birthday" in event.name: 
                    # print(f"Event: {event.name}, Start: {occurrence}, End: {end_time}")
                    asdf.append(event.name, occurrence, end_time)
        else:
            # print(f"Event: '{event.name}', Start: {event.begin}, End: {event.end}")
            asdf.append([event.name, event.begin, event.end])
            # print("here")


ics_file = 'C:/Users/Florian/Downloads/mntg.florian@gmail.com.ical/mntg.florian@gmail.com.ics'
list_events(ics_file)
# print(asdf)
for x in asdf:
    if "Arbeit" in x[0] or "Schule" in x[0]:
        print(x)