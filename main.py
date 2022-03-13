#Zulu to CST
from datetime import datetime
from pytz import timezone

fmt = "%Y/%m/%d %I:%M:%S"
timezonelist = ['Zulu','US/Central']
for zone in timezonelist:
    now_time = datetime.now(timezone(zone))
    print(now_time.strftime(fmt))