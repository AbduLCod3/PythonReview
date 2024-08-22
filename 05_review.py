# value = True

# while value:
#     print(value)
#     value = False # We can set value = 0 and it is the sames as false

value = 'y'
count  = 0

while value:
    count += 1
    print(count)
    if (count == 5 ):
        break
    else:
        value = 0 # we are setting value to false
        continue