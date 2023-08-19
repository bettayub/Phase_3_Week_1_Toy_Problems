def my_time_to_24hr(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour_24 = 0