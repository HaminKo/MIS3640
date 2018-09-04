import math

# What is the volume of a sphere with radius 5?

radius = 5
sphere_volume = (4/3) * math.pi * radius ** 3 

print('The volume of a sphere with a radius of 5 is {:.2f}'.format(sphere_volume))

# Suppose the cover price of a book is $24.95, but bookstores get a 40\% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

book_price = 24.95
discount = .4
first_shipment = 3
additional_shipment = .75
book_amount = 60

wholesale_cost = book_amount * (book_price * (1 - discount)) + first_shipment + (book_amount - 1) * (additional_shipment)

print('The wholesale cost for 60 copies is {:.2f}'.format(wholesale_cost))

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?

minute = 60
hour = minute * 60
start_time = 6 * hour + 52 * minute
easy_pace = 8 * minute + 15
tempo_pace = 7 * minute + 12
easy_miles = 2
tempo_miles = 3

run_time = easy_pace * easy_miles + tempo_pace * tempo_miles
end_time = run_time + start_time

print('You will be home for breakfast at {}:{}'.format(end_time//hour, (end_time%hour)//minute))

#If my average grade rises from 82 to 89. What is the percentage of the increase? Format the result as 'xx.x%'. Keep one figure after decimal point.

grade_start = 82
grade_end = 89

percentage_increase = (grade_end/grade_start - 1) * 100

print('The percentage increase is {:.1f}%'.format(percentage_increase))