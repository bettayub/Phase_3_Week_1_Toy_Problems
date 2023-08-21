def my_time_to_24hr(hour, minute, period): #defining a function
    if period == "am":
        if hour == 12:
            hour_24 = 0
        else:
            hour_24 = hour
    else:  # period == "pm"
        if hour == 12:
            hour_24 = 12
        else:
            hour_24 = hour + 12
    
    return f"{hour_24:02d}{minute:02d}"


# List of test cases: (hour, minute, period)
test_cases = [
    (8, 30, "pm"),
    (1, 30, "am"),
    (12, 15, "am"),
    (12, 00, "m")
]


# Loop through test cases
for hour, minute, period in test_cases:
    converted_time = my_time_to_24hr(hour, minute, period)
    print(f"{hour:02d}:{minute:02d} {period.upper()} -> {converted_time}")

    # how to run
    # python3 Time.py