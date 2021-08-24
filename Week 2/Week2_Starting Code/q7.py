# This line of code prompts the user for a system time.
input_str = input('Please enter the system time (in seconds): ')

################################################################################
# Complete the code below to get the correct numbers of days, hours, minutes and seconds.

num_days = 0
num_hours = 0
num_minutes = 0
num_seconds = 0

# Put your code below
system_time = int(input_str)

day_in_seconds = 60 * 60 * 24
hour_in_seconds = 60 * 60
minute_in_seconds = 60

num_days = system_time // day_in_seconds
num_hours = (system_time - (num_days * day_in_seconds)) // hour_in_seconds
num_minutes = (system_time - (num_days * day_in_seconds) - (num_hours * hour_in_seconds)) // minute_in_seconds
num_seconds = (system_time - (num_days * day_in_seconds) - (num_hours * hour_in_seconds) - (num_minutes * minute_in_seconds))



################################################################################
# DO NOT MODIFY THE CODE BELOW!!!

# This line of code displays the results.
print('Based on this system time, ' + str(num_days) + ' days, ' + str(num_hours) + ' hours, ' + str(num_minutes) + ' minutes and ' + str(num_seconds) + ' seconds have passed since 1 January 1970 00:00:00 UT.')