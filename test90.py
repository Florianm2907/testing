import sys
from icalendar import Calendar, Event
from datetime import datetime, timedelta

def expand_recurring_events(event):
    """ Expand recurring events into individual instances """
    recurring_events = []

    # Get start and end times for the original event
    start_time = event.get('dtstart').dt
    end_time = event.get('dtend').dt
    duration = end_time - start_time if end_time else timedelta(days=1)  # Default duration if no end time

    # Handle daily recurring events
    if 'RRULE' in event:
        rrule = event['RRULE'].to_ical().decode('utf-8')
        if 'DAILY' in rrule:
            start = event['DTSTART'].dt
            end = event['DTEND'].dt

            delta = timedelta(days=1)
            while start <= end:
                recurring_event = Event()
                recurring_event['SUMMARY'] = event['SUMMARY']
                recurring_event['DTSTART'] = start
                recurring_event['DTEND'] = start + duration
                recurring_events.append(recurring_event)
                start += delta

    else:
        recurring_events.append(event)

    return recurring_events

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

                    event_start = component.get('dtstart').dt
                    event_end = component.get('dtend').dt

                    if event_end is None:
                        continue  # Skip events without end time

                    # Handle recurring events
                    if 'RRULE' in component:
                        recurring_events = expand_recurring_events(component)
                    else:
                        recurring_events = [component]

                    for event in recurring_events:
                        event_start = event.get('DTSTART').dt
                        event_end = event.get('DTEND').dt

                        if "Schule" in event_summary:
                            event_duration = timedelta(hours=8)  # Always 8 hours for "Schule" events
                        else:
                            event_duration = event_end - event_start

                        # Determine the week of the event
                        week_start = event_start - timedelta(days=event_start.weekday())
                        week_start = datetime.combine(week_start, datetime.min.time())

                        # Add the duration to the appropriate week
                        if week_start not in event_durations:
                            event_durations[week_start] = timedelta()

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
                    event_start = component.get('dtstart').dt
                    event_end = component.get('dtend').dt
                    
                    # Handle recurring events
                    if 'RRULE' in component:
                        recurring_events = expand_recurring_events(component)
                    else:
                        recurring_events = [component]

                    for event in recurring_events:
                        event_start = event.get('DTSTART').dt
                        event_end = event.get('DTEND').dt
                        
                        # Check if the event has an end time
                        if event_end and isinstance(last_14_days_start, datetime) and isinstance(event_start, datetime):
                            # Check if the event is in the last 14 days
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
