# Write a function named add_time that takes in two required parameters
# and one optional parameter:
#     a start time in the 12-hour clock format(ending in AM or PM)
#     a duration time that indicates the number of hours and minutes
#     (optional) a starting day of the week, case insensitive

# The function should add the duration time to the start time and
# return the result.

# If the result will be the next day, it should show(next day) after the time.
# If the result will be more than one day later, it should show(n days later)
# after the time, where "n" is the number of days later.

# If the function is given the optional starting day of the week parameter,
# then the output should display the day of the week of the result.
# The day of the week in the output should appear after the time and before
# the number of days later.

def add_time(start, duration, input_day=None):

    start_list = start.split()  # ['00:00','?M']
    start_list[0] = start_list[0].split(':')  # [['00','00'],'?M']

    start_mins = int(start_list[0][0])*60 + \
        int(start_list[0][1])  # start time in minutes

    if start_list[1] == 'PM':
        start_mins += 720  # if PM => +12 h in mins

    dur_list = duration.split(':')  # ['00','00']
    dur_mins = int(dur_list[0])*60 + int(dur_list[1])  # duration in mins

    dur_total = (start_mins + dur_mins)  # total time in mins
    hours = dur_total // 60  # total time in hours
    minutes = dur_total - hours * 60  # minutes left

    # after duration, is it AM or PM?
    if (dur_total//720) % 2 == 0:
        am_pm = 'AM'
    else:
        am_pm = 'PM'

    # how many days takes
    days = hours//24

    # final format for print: hours from 1 to 12
    hour = hours - (hours//12)*12
    if hour == 0:
        hour = 12

    # ------------------WEEK DAYS------------------------

    week_list = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # optional argument is given (not None)
    if input_day:
        # take optional argument => index for the week_list
        cod_sem = week_list.index(str(input_day).capitalize())

        # looping the list: after 6 comes 0
        counter = days
        while counter > 0:
            if cod_sem == 6:
                cod_sem = 0
            else:
                cod_sem += 1
            counter -= 1

        if days > 1:
            # to avoid mins with only a digit (<10), f-string has a way (:02d)
            output = (
                f'{hour}:{minutes:02d} {am_pm}, {week_list[cod_sem]} ({days} days later)')
        elif days == 1:
            output = (
                f'{hour}:{minutes:02d} {am_pm}, {week_list[cod_sem]} (next day)')
        else:
            output = (f'{hour}:{minutes:02d} {am_pm}, {week_list[cod_sem]}')

    # optional argument not provided (=None)
    else:
        if days > 1:
            output = (f'{hour}:{minutes:02d} {am_pm} ({days} days later)')
        elif days == 1:
            output = (f'{hour}:{minutes:02d} {am_pm} (next day)')
        else:
            output = (f'{hour}:{minutes:02d} {am_pm}')

    return output


print(add_time("11:06 PM", "2:02"))
add_time("3:30 PM", "2:12")
add_time("11:55 AM", "3:12")
