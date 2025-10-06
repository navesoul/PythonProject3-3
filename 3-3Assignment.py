# START
print("Date Validation Program")
invalidDate = False
validDate = True

# Set values
month = 5
day = 32
year = 2014

# Validate year
if year <= 0:
    invalidDate = True
# Validate month
elif month < 1 or month > 12:
    invalidDate = True
# Validate day based on month
elif day < 1 or day > 31:
    invalidDate = True
# Check specific month day limits
elif month in [4, 6, 9, 11] and day > 30:
    invalidDate = True
# Check February (28 days max, no leap year)
elif month == 2 and day > 28:
    invalidDate = True

# Output the result
if invalidDate:
    print(f"{month}/{day}/{year} is an invalid date.")
else:
    print(f"{month}/{day}/{year} is a valid date.")