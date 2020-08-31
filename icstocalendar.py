# Inspirert av https://stackoverflow.com/questions/3408097/parsing-files-ics-icalendar-using-python
from icalendar import Calendar, vDatetime
from datetime import datetime

icsfile = input()
g = open(icsfile,'r')
gcal = Calendar.from_ical(g.read())

for component in gcal.walk():

    if component.name == "VEVENT":
        description = component.get('description')
        summary = component.get('summary')
        location = component.get('location')
        datebytes = vDatetime.to_ical(component['dtstart'])
        date = datebytes.decode("utf-8")
        dt = datetime.strptime(date, '%Y%m%dT%H%M%SZ')
        mmdd = str(dt.month) + '\\' + str(dt.day)
        hhmm = str(dt.hour) + ':' + str(dt.minute)
        print(mmdd, '\t', hhmm, summary, location)
        

g.close()

