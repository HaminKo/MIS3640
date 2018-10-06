import math

def binary_search(my_list, x):
    '''
    this function adopts bisection/binary search to find the index of a given
    number in an ordered list
    my_list: an ordered list of numbers from smallest to largest
    x: a number
    returns the index of x if x is in my_list, None if not.
    '''
    pass
    index = round(len(my_list)/2)
    move = round(len(my_list)/4)
    index_searched = []
    while True:
        print("Printing index: {}".format(index))
        if my_list[index] < x:
            index = index + move
        elif my_list[index] > x:
            index = index - move
        if my_list[index] == x:
            return index
        if index in index_searched or index <= 0 or index >= len(my_list) - 1:
            return "None"
        index_searched.append(index)
        move = math.ceil(move/2)


test_list = [1, 3, 5, 235425423, 23, 6, 0, -23, 6434]
test_list.sort()
# [-23, 0, 1, 3, 5, 6, 23, 6434, 235425423]

print(binary_search(test_list, -23))
print(binary_search(test_list, 0))
print(binary_search(test_list, 235425423))
print(binary_search(test_list, 30))

# expected output
# 0
# 1
# 8
# None