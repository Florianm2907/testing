import sys
from icalendar import Calendar
from datetime import datetime, timedelta

def list_filtered_events(ics_file):
    try:
        with open(ics_file, 'rb') as file:
            calendar = Calendar.from_ical(file.read())

            event_durations = {}

            for component in calendar.walk():
                if component.name == "VEVENT":
                    event_summary = component.get('summary')
                    if not event_summary:
                        continue
                    event_summary = str(event_summary)

                    event_start = component.get('dtstart')
                    event_end = component.get('dtend')

                    if event_start and event_end:
                        event_start = event_start.dt
                        event_end = event_end.dt

                        if "Arbeit" in event_summary or "Schule" in event_summary:
                            # Calculate the duration of the event
                            event_duration = event_end - event_start

                            # Determine the week of the event
                            week_start = event_start - timedelta(days=event_start.weekday())
                            week_start = week_start.replace(hour=0, minute=0, second=0, microsecond=0)

                            # Add the duration to the appropriate week
                            if week_start not in event_durations:
                                event_durations[week_start] = timedelta()

                            # For "Schule" events, add 8 hours regardless of actual duration
                            if "Schule" in event_summary:
                                event_durations[week_start] += timedelta(hours=8)
                            else:
                                event_durations[week_start] += event_duration

            print("Weekly durations for 'Arbeit' or 'Schule' events:")
            for week_start, duration in sorted(event_durations.items()):
                # Convert duration to hours
                total_hours = duration.total_seconds() / 3600
                print(f"Week starting {week_start}: {total_hours:.2f} hours")

            # Print events in the last 14 days for debugging
            print("\nEvents in the last 14 days:")
            last_event_start = max(event_durations.keys(), default=datetime.now())
            last_14_days_start = last_event_start - timedelta(days=14)
            for component in calendar.walk():
                if component.name == "VEVENT":
                    event_summary = component.get('summary')
                    event_start = component.get('dtstart')
                    event_end = component.get('dtend')
                    
                    if event_start and event_end:
                        event_start = event_start.dt
                        event_end = event_end.dt
                        
                        # Check if the event is in the last 14 days
                        if isinstance(last_14_days_start, datetime) and isinstance(event_start, datetime):
                            if event_start >= last_14_days_start and event_start <= last_event_start:
                                print(f"Summary: {event_summary}")
                                print(f"Start: {event_start}")
                                print(f"End: {event_end}")
                                print("\n")


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python list_events_with_filter.py <path_to_ics_file>")
    else:
        ics_file = sys.argv[1]
        list_filtered_events(ics_file)
