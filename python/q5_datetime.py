from datetime import datetime

date_start = '01-02-2013'
date_stop = '07-28-2015'

def computeDays(start, stop,frmt):
    result = datetime.strptime(stop,frmt) - datetime.strptime(start,frmt);
    return "Days: " + str(result.days)

print computeDays(date_start,date_stop,"%m-%d-%Y")

date_start = '12312013'
date_stop = '05282015'

print computeDays(date_start,date_stop,"%m%d%Y")

date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

print computeDays(date_start,date_stop,"%d-%b-%Y")
