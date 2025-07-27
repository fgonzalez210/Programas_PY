def add_time(start, duration, day=None):
    # Days of the week for reference
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Parsing start time
    time_part, meridiem = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))

    # Converting start time to 24-hour format
    if meridiem == 'PM' and start_hour != 12:
        start_hour += 12
    elif meridiem == 'AM' and start_hour == 12:
        start_hour = 0

    # Parsing duration
    dur_hour, dur_minute = map(int, duration.split(':'))

    # Adding time
    total_minutes = start_minute + dur_minute
    extra_hours = total_minutes // 60
    final_minute = total_minutes % 60

    total_hours = start_hour + dur_hour + extra_hours
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # Converting back to 12-hour format
    if final_hour_24 == 0:
        final_hour = 12
        final_meridiem = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_meridiem = 'AM'
    elif final_hour_24 == 12    :
        final_hour = 12
        final_meridiem = 'PM'
    else:
        final_hour = final_hour_24 - 12
        final_meridiem = 'PM'

    # Build the result string
    new_time = f"{final_hour}:{final_minute:02d} {final_meridiem}"

    # Add day of week if provided
    if day:
        day_index = days_of_week.index(day.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    # Add day information
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
