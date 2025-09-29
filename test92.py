import sys
import os
from datetime import datetime
from icalendar import Calendar, Event
from dateutil import rrule
from dateutil.parser import parse as date_parse

def parse_rrule_params(rrule_str):
    rrule_params = {}
    if rrule_str:
        rrule_str = rrule_str.replace('VRECUR({', '').replace('})', '')
        params = rrule_str.split(',')
        for param in params:
            if '=' in param:
                key, value = param.split('=', 1)
                rrule_params[key.strip()] = value.strip("'")
    return rrule_params

def unpack_recurring_events(input_file, output_file):
    with open(input_file, 'rb') as f:
        calendar = Calendar.from_ical(f.read())

    new_calendar = Calendar()

    for component in calendar.walk():
        if component.name == "VEVENT":
            if component.get('RRULE'):
                # Extract and parse RRULE string
                rrule_str = str(component.decoded('RRULE'))
                rrule_params = parse_rrule_params(rrule_str)
                
                # Get necessary RRULE parameters
                freq = rrule_params.get('FREQ', None)
                dtstart = component.decoded('DTSTART')
                
                if freq and isinstance(dtstart, datetime):
                    # Construct rrule object
                    until_str = rrule_params.get('UNTIL')
                    if until_str:
                        until = date_parse(until_str)
                        occurrences = rrule.rrulestr(f"FREQ={freq};UNTIL={until_str};", dtstart=dtstart)
                    else:
                        count = int(rrule_params.get('COUNT', 0))
                        occurrences = rrule.rrulestr(f"FREQ={freq};COUNT={count};", dtstart=dtstart)
                    
                    for occurrence in occurrences:
                        new_event = Event()
                        new_event.add('summary', component.get('summary'))
                        new_event.add('dtstart', occurrence)
                        if component.get('DTEND'):
                            duration = component.decoded('DTEND') - dtstart
                            new_event.add('dtend', occurrence + duration)
                        new_calendar.add_component(new_event)
            else:
                # Single instance event
                new_calendar.add_component(component)

    with open(output_file, 'wb') as f:
        f.write(new_calendar.to_ical())

    print(f"Unpacked recurring events from {input_file} to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file.ics output_file.ics")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith('.ics') or not os.path.isfile(input_file):
        print(f"Error: Input file {input_file} is not a valid .ics file")
        sys.exit(1)

    unpack_recurring_events(input_file, output_file)
