print("1. How many seconds are there in 42 minutes 42 seconds?\n")

seconds = 42 * 60 + 42
print(str(seconds) + " seconds\n")

print("2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.\n")

miles = 10 / 1.61
print(str(round(miles, 2)) + " miles\n")

print("3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?\n")


print(str(round( ( (seconds / miles)/60) - 0.5) ) + " minutes and " + str(round( (seconds/miles)%60, 2) ) + " seconds per mile\n")

print(str(round( (miles) / ( (seconds) / 3600), 2) ) + " miles per hour\n")