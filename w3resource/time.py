import time
from datetime import datetime, date
from time import strftime

from pyspark.examples.src.main.python.streaming.network_wordjoinsentiments import print_happiest_words

# Display the current time in various formats
dt = date.today()
print(dt)

dt1 = datetime.today()
print(dt1)

dt2 = datetime.now()
print(dt2)

str = dt2.strftime('Date = %d, %B, %y %H:%M:%S, today is %a or %A and week day number is %w and month is %m or %B')
print(str)

str = dt.strftime('Today is the %j th day of the year')
print(str)

# Display the current time in seconds since epoch
seconds_since_epoch = time.time()
print(f"Seconds since epoch: {seconds_since_epoch}")

str = dt.strftime('And it is %A')
print(str)

str = strftime('Current time is = %H:%M:%S')
print(str)
