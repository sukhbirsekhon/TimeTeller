# The goal of the script is to tell you current date and time

from datetime import datetime

# Using datetime module, extract current timestamp
current = datetime.now()

# Extract today's date from current timestamp
date = current.strftime("%d %b, %Y")

# Extract current time from current timestamp
time = current.strftime("%I:%M:%S %p")

# Print today's date and time
print("Today's date is " + str(date))
print("and Current time is " + str(time))