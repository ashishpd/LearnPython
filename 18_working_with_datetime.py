"""
18_working_with_datetime.py

This file demonstrates working with dates and times in Python.
The datetime module provides classes for manipulating dates and times.
"""

from datetime import datetime, date, time, timedelta

# CURRENT DATE AND TIME

# Get current date and time
now = datetime.now()
print(f"Current date and time: {now}")

# Get current date only
today = date.today()
print(f"Today's date: {today}")

# Get current time only (manually)
current_time = datetime.now().time()
print(f"Current time: {current_time}")

# CREATING DATE/TIME OBJECTS

# Create a specific date
specific_date = date(2023, 12, 25)
print(f"\nSpecific date: {specific_date}")

# Create a specific time
specific_time = time(14, 30, 0)  # 2:30:00 PM
print(f"Specific time: {specific_time}")

# Create a specific datetime
specific_datetime = datetime(2023, 12, 25, 14, 30, 0)
print(f"Specific datetime: {specific_datetime}")

# FORMATTING DATES AND TIMES

# strftime() - format datetime to string
now = datetime.now()

formats = {
    "Full date": now.strftime("%Y-%m-%d"),
    "Date with time": now.strftime("%Y-%m-%d %H:%M:%S"),
    "Readable date": now.strftime("%B %d, %Y"),
    "Time only": now.strftime("%I:%M %p"),
    "Day of week": now.strftime("%A"),
}

print("\nDate formats:")
for label, formatted in formats.items():
    print(f"  {label}: {formatted}")

# PARSING DATES FROM STRINGS

# strptime() - parse string to datetime
date_string = "2023-12-25 14:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"\nParsed date: {parsed_date}")

# DATE/TIME ARITHMETIC

# Adding and subtracting time
now = datetime.now()

# Add days
future = now + timedelta(days=7)
print(f"\nToday: {now.strftime('%Y-%m-%d')}")
print(f"In 7 days: {future.strftime('%Y-%m-%d')}")

# Subtract days
past = now - timedelta(days=30)
print(f"30 days ago: {past.strftime('%Y-%m-%d')}")

# Add hours, minutes, seconds
future_time = now + timedelta(hours=2, minutes=30)
print(f"\nIn 2.5 hours: {future_time.strftime('%H:%M:%S')}")

# Calculate difference between dates
date1 = datetime(2023, 1, 1)
date2 = datetime(2023, 12, 31)
difference = date2 - date1
print(f"\nDays between Jan 1 and Dec 31, 2023: {difference.days}")

# COMPONENTS OF DATE/TIME

now = datetime.now()

print(f"\nDate components:")
print(f"  Year: {now.year}")
print(f"  Month: {now.month}")
print(f"  Day: {now.day}")
print(f"  Hour: {now.hour}")
print(f"  Minute: {now.minute}")
print(f"  Second: {now.second}")
print(f"  Microsecond: {now.microsecond}")
print(f"  Weekday (0=Monday): {now.weekday()}")
print(f"  Weekday name: {now.strftime('%A')}")

# REPLACING DATE/TIME COMPONENTS

original = datetime(2023, 1, 15, 10, 30, 0)
new_datetime = original.replace(year=2024, month=6)
print(f"\nOriginal: {original}")
print(f"Replaced: {new_datetime}")

# COMPARING DATES

date1 = datetime(2023, 1, 1)
date2 = datetime(2023, 6, 15)
date3 = datetime(2023, 6, 15)

print(f"\nDate comparisons:")
print(f"date1 < date2: {date1 < date2}")
print(f"date2 > date1: {date2 > date1}")
print(f"date2 == date3: {date2 == date3}")
print(f"date1 >= date2: {date1 >= date2}")

# TIMEZONES (using pytz - external library)
# Standard library datetime supports timezone-naive and timezone-aware

from datetime import timezone, timedelta

# Create timezone-aware datetime
utc_now = datetime.now(timezone.utc)
print(f"\nUTC time: {utc_now}")

# Create custom timezone (UTC+5:30 for example)
custom_tz = timezone(timedelta(hours=5, minutes=30))
local_time = datetime.now(custom_tz)
print(f"Custom timezone (+5:30): {local_time}")

# WORKING WITH TIMEDELTA

# Create timedelta objects
delta1 = timedelta(days=5, hours=3, minutes=30)
delta2 = timedelta(weeks=2)
delta3 = timedelta(hours=12)

print(f"\nTimedelta examples:")
print(f"5 days, 3 hours, 30 minutes: {delta1}")
print(f"2 weeks: {delta2}")
print(f"12 hours: {delta3}")
print(f"Total seconds in delta1: {delta1.total_seconds()}")

# PRACTICAL EXAMPLES

# Calculate age
def calculate_age(birth_date):
    """Calculate age from birth date."""
    today = date.today()
    age = today.year - birth_date.year
    # Adjust if birthday hasn't occurred this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

birth_date = date(1990, 5, 15)
age = calculate_age(birth_date)
print(f"\nAge calculation:")
print(f"Born: {birth_date}, Age: {age}")

# Countdown to a date
target_date = datetime(2024, 12, 31, 23, 59, 59)
now = datetime.now()
time_left = target_date - now

print(f"\nTime until Dec 31, 2024:")
print(f"  Days: {time_left.days}")
print(f"  Total seconds: {int(time_left.total_seconds())}")

# Format duration
def format_duration(seconds):
    """Format seconds into readable duration."""
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{days} days, {hours} hours, {minutes} minutes, {secs} seconds"

duration = 3661  # 1 hour, 1 minute, 1 second
print(f"\nDuration formatting:")
print(f"{duration} seconds = {format_duration(duration)}")

