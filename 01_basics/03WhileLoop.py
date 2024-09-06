x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x += 1


numbers = list(range(1, 21))
# Break example 
print('Break example')
for item in numbers:
    if item == 5:
        break
    print(item)


# Continue example
print('Continue example')
for item in numbers: 
    if item % 2 == 0:
# continue will skip the even numbers. continue will skip the rest of the code and go to the next iteration or top of the loop        
        continue
    print(item)


# pass example
print('Pass example')
# you can ot have empty loop in python, so you can use pass to avoid syntax error
for items in numbers:
    # do nothing
    pass