from icalendar import Calendar, Event
from datetime import datetime
from dateutil.rrule import rrulestr
from dateutil.tz import tzutc

def convert_to_utc(dt):
    """Converts a datetime object to UTC."""
    if isinstance(dt, datetime) and dt.tzinfo is not None:
        return dt.astimezone(tzutc()).replace(tzinfo=None)
    return dt

def format_until(dt):
    """Formats the UNTIL parameter in UTC as required by iCalendar specification."""
    if isinstance(dt, datetime):
        return dt.strftime('%Y%m%dT%H%M%SZ')
    return dt

def expand_recurring_events(ics_file):
    with open(ics_file, 'rb') as file:
        calendar = Calendar.from_ical(file.read())
        new_calendar = Calendar()

        for component in calendar.walk():
            if component.name == "VEVENT":
                rrule = component.get('rrule')
                if rrule:
                    rrule_str = rrule.to_ical().decode('utf-8')
                    dtstart = component.get('dtstart').dt
                    dtend = component.get('dtend').dt

                    # Ensure DTSTART is datetime and convert to UTC if needed
                    if isinstance(dtstart, datetime):
                        dtstart = convert_to_utc(dtstart)
                    else:
                        continue  # Skip if DTSTART is not datetime

                    # Format UNTIL parameter in UTC
                    if 'UNTIL=' in rrule_str:
                        until_idx = rrule_str.index('UNTIL=')
                        until_end_idx = rrule_str.index(';', until_idx) if ';' in rrule_str[until_idx:] else None
                        replace_text = 'UNTIL=' + format_until(dtstart) + (';' if until_end_idx is not None else '')
                        rrule_str = rrule_str[:until_idx] + replace_text + (rrule_str[until_end_idx:] if until_end_idx is not None else '')

                    # Expand recurring events
                    try:
                        for dt in rrulestr(rrule_str, dtstart=dtstart):
                            new_event = Event()
                            new_event.add('summary', component.get('summary'))
                            
                            # Convert dt to UTC for DTSTART and DTEND
                            if isinstance(dt, datetime):
                                dt = convert_to_utc(dt)
                                new_event.add('dtstart', dt)
                                new_event.add('dtend', dt + (dtend - dtstart))
                            else:
                                new_event.add('dtstart', dtstart)
                                new_event.add('dtend', dtend)
                            
                            new_calendar.add_component(new_event)
                    except ValueError as e:
                        print(f"Error expanding recurring event: {e}")
                else:
                    # For non-recurring events, just copy over
                    new_calendar.add_component(component)

        # Save expanded calendar to a new file
        with open('expanded_file', 'wb') as new_file:
            new_file.write(new_calendar.to_ical())

if __name__ == "__main__":
    ics_file = 'C:/Users/Florian/Downloads/mntg.florian@gmail.com.ical/mntg.florian@gmail.com.ics'  # Replace with your ICS file
    expand_recurring_events(ics_file)
