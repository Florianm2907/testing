from ics import Calendar
from datetime import datetime, timedelta
from collections import defaultdict
from dateutil.rrule import rrulestr
import pytz
import re
asdf = []
def convert_until_to_utc(until_str):
    # Parse UNTIL value from RRULE string
    until_dt = datetime.strptime(until_str, '%Y%m%dT%H%M%SZ')
    
    # Convert to UTC if not already
    if until_dt.tzinfo is not None:
        until_dt = until_dt.astimezone(pytz.utc)
    
    return until_dt

def calculate_total_duration(events):
    total_duration = 0
    
    # Convert and sort events by start time
    sorted_events = sorted(events, key=lambda x: datetime.fromisoformat(x[0]))

    # Iterate through sorted events
    for start_str, end_str in sorted_events:
        start = datetime.fromisoformat(start_str)
        end = datetime.fromisoformat(end_str)
        
        # Calculate duration in hours (assuming end > start)
        duration = (end - start).total_seconds() / 3600  # Convert seconds to hours
        total_duration += duration
    
    return total_duration

def calculate_total_duration_by_day(events):
    total_duration_by_day = defaultdict(float)
    
    # Convert and sort events by start time
    sorted_events = sorted(events, key=lambda x: datetime.fromisoformat(x[0]))
    
    # Iterate through sorted events
    for start_str, end_str in sorted_events:
        start = datetime.fromisoformat(start_str)
        end = datetime.fromisoformat(end_str)
        
        # Calculate duration in hours (assuming end > start)
        duration = (end - start).total_seconds() / 3600  # Convert seconds to hours
        if duration == 7.25: duration = 8
        # Calculate day start (midnight) and add duration to the respective day
        day_start = start.replace(hour=0, minute=0, second=0, microsecond=0)
        total_duration_by_day[day_start] += duration
    
    return total_duration_by_day

def calculate_total_duration_by_week(events):
    total_duration_by_week = defaultdict(float)
    
    # Convert and sort events by start time
    sorted_events = sorted(events, key=lambda x: datetime.fromisoformat(x[0]))
    
    # Iterate through sorted events
    for start_str, end_str in sorted_events:
        start = datetime.fromisoformat(start_str)
        end = datetime.fromisoformat(end_str)
        
        # Calculate duration in hours (assuming end > start)
        duration = (end - start).total_seconds() / 3600  # Convert seconds to hours
        if duration == 7.25: duration = 8
        
        # Calculate week start (Monday) and add duration to the respective week
        week_start = start - timedelta(days=start.weekday())
        total_duration_by_week[week_start] += duration
    
    return total_duration_by_week

def list_events(ics_file):
    with open(ics_file, 'r', encoding='utf-8') as f:
        c = Calendar(f.read())
    
    for event in c.events:
        # Check if 'RRULE' exists in event's extra attributes
        if 'RRULE' in str(event):
            rule = str(event).splitlines()[1][6:]
            # Parse UNTIL value and convert to UTC
            until_match = re.search(r'UNTIL=(\d{8}T\d{6}Z)', rule)
            if until_match:
                until_str = until_match.group(1)
                until_dt = convert_until_to_utc(until_str)
                rule = rule.replace(until_str, until_dt.strftime('%Y%m%dT%H%M%SZ'))

            # Generate occurrences based on RRULE
            if "UNTIL" in rule and len(rule[rule.index("UNTIL")+6:rule.index("INTERVAL")]) < 10: rule = rule.replace(rule[rule.index("UNTIL")+6:rule.index("UNTIL")+14], rule[rule.index("UNTIL")+6:rule.index("UNTIL")+14] + "T000000Z;" + rule[rule.index("UNTIL")+15:])
            occurrences = rrulestr(rule, dtstart=event.begin.datetime)
            for occurrence in occurrences:
                # Adjust the occurrence time to local timezone
                # occurrence_local = occurrence.astimezone(pytz.timezone('Europe/Berlin'))
                occurrence_local = occurrence
                # Calculate end time based on duration or difference between start and end times
                if event.duration:
                    end_time = occurrence_local + event.duration
                else:
                    end_time = occurrence_local + (event.end - event.begin)
                
                # if not "Geburtstag" in event.name and not "birthday" in event.name and not "Heiligabend" in event.name: print(f"Event: {event.name}, Start: {occurrence_local}, End: {end_time}")
                if "Arbeit" in event.name or "Schule" in event.name: 
                    # print(f"Event: {event.name}, Start: {occurrence_local}, End: {end_time}")
                    asdf.append([str(occurrence_local), str(end_time)])
        else:
            if "Arbeit" in event.name or "Schule" in event.name: 
                # print(f"Event: {event.name}, Start: {event.begin}, End: {event.end}")
                asdf.append([str(event.begin), str(event.end)])
            
# Example usage:
ics_file = 'C:/Users/Florian/Downloads/mntg.florian@gmail.com.ical/mntg.florian@gmail.com.ics'
list_events(ics_file)
print(calculate_total_duration(asdf))
total_duration_by_week = calculate_total_duration_by_week(asdf)
total_duration_by_day = calculate_total_duration_by_day(asdf)

# for week_start, total_duration in sorted(total_duration_by_week.items()):
#     print(f"Week starting on {week_start.strftime('%Y-%m-%d')}: Total duration = {total_duration:.2f} hours")
asdf1 = []
for day_start, total_duration in sorted(total_duration_by_day.items()):
    # print(f"Day {day_start.strftime('%Y-%m-%d')}: Total duration = {total_duration:.2f} hours")
    asdf1.append([day_start.strftime('%Y%m%d'), total_duration])

# print(asdf1)



aggregated_data = {}
asdf2 =[]
# Iterate through the list of lists
for date_str, value in asdf1:
    if date_str in aggregated_data:
        # If date is already in dictionary, add the value to existing total
        aggregated_data[date_str] += value
    else:
        # If date is not in dictionary, initialize with current value
        aggregated_data[date_str] = value

# Convert dictionary back to list of lists (if needed)
aggregated_list = [[date_str, total_value] for date_str, total_value in aggregated_data.items()]

# Output aggregated data
for date_str, total_value in aggregated_list:
    # print(f"Date: {date_str}, Total value: {total_value}")
    asdf2.append([date_str, total_value])

print(asdf2)
print(len(asdf2))


weekly_totals = defaultdict(float)

# Iterate through the list of lists
for date_str, total_value in asdf2:
    # Calculate week start (assuming Monday as start of week)
    week_start = datetime.strptime(date_str, '%Y%m%d').date() - timedelta(days=datetime.strptime(date_str, '%Y%m%d').date().weekday())
    
    # Add total_value to the respective week
    weekly_totals[week_start] += total_value

# Output weekly totals
for week_start, total_value in sorted(weekly_totals.items()):
    print(f"Week starting on {week_start}: Total value = {total_value}")

for week_start, total_value in sorted(weekly_totals.items()):
    print(total_value)