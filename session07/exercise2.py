# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 


# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# Rewrite exercise 1 with while loops:

num = 0
count = 1
while count <= 10:
    num += count
    count += 1
print(num)

num2 = 0
count2 = 1
while count2 <= 1000:
    num2 += count2
    count2 += 1
print(num2)

num3 = 0
count3 = 1
while count3 <= 1000:
    num3 += count3
    count3 += 2
print(num3)