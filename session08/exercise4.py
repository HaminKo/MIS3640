def price(word):
    total = 0
    for letter in word.lower():
        if ord(letter) >= 97 and ord(letter) <= 122:
            total = total + ord(letter) - 96
    return total

def print_receipt(items):
    total_cost = 0
    for item in items:
        total_cost += price(item)
        print('{:21}{:>8}'.format(
            item, '$' + str(price(item)) + '.00'
        ))
    print('{:28}'.format('-----------------------------'))
    print('{:21}{:>8}'.format(
        'Total', '$' + str(total_cost) + '.00'
        ))

food = ['bananas', 'rice', 'paprika', 'potato chips']
print_receipt(food)