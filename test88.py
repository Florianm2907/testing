import sys
from icalendar import Calendar
from datetime import datetime, timedelta

def list_and_sum_events(ics_file):
    try:
        with open(ics_file, 'rb') as file:
            calendar = Calendar.from_ical(file.read())
            
            total_duration = timedelta()
            print("Events in the ICS file containing 'Arbeit' or 'Schule':")
            for component in calendar.walk():
                if component.name == "VEVENT":
                    event_summary = component.get('summary')
                    if event_summary and ('Arbeit' in event_summary or 'Schule' in event_summary):
                        event_start = component.get('dtstart').dt if component.get('dtstart') else None
                        event_end = component.get('dtend').dt if component.get('dtend') else None
                        
                        if event_start and event_end:
                            duration = event_end - event_start
                            total_duration += duration
                            
                            event_location = component.get('location') if component.get('location') else "No location"
                            
                            print(f"Summary: {event_summary}")
                            print(f"Start: {event_start}")
                            print(f"End: {event_end}")
                            print(f"Duration: {duration}")
                            print(f"Location: {event_location}")
                            print("\n")
            
            print(f"Total duration of events containing 'Arbeit' or 'Schule': {total_duration}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python list_events.py <path_to_ics_file>")
    else:
        ics_file = sys.argv[1]
        list_and_sum_events(ics_file)
