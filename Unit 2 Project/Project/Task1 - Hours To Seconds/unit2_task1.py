"""
This program asks for the number of hours, minutes, and seconds, then calculates and shows the total equivalent number of seconds.Date: January 1, 2025

Author: First Last
Date: January 1, 2025
Version: 1.0
"""
SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

# Prompting for input
hours = int(input('Enter the number of hours: '))
minutes = int(input('Enter the number of minutes: '))
seconds = int(input('Enter the number of seconds: '))

# Calculating total seconds
total_seconds = (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE) + seconds

# Displaying the result
print(f'{hours} hours, {minutes} minutes, and {seconds} seconds is equal to {total_seconds} total seconds.')
