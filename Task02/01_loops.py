### While loop
value = 0
# while value <=10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <=10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
    
# else:
#     print("Loop is completed. Value is now equal to " + str(value))

names = ['Abdul', 'Adam', 'John']
actions = ['codes', 'eats', 'sleeps']
# for x in names:
#     print(x)

# for x in 'Mississippi':
#     print(x)

# for name in names:
#     if name == 'Adam':
#         break
#     print(name)

# for name in names:
#     if name == 'Adam':
#         continue
#     print(name)

# for x in range(4):
#     print(x)
    
# for x in range(2, 4):
#     print(x)

# for x in range(0, 101, 5):
#     print(x)
# else:
#     print('Glad that\'s over!')

# for name in names:
#     for action in actions:
#         print(name +  " " + action + '.')

for action in actions:
    for name in names:
        print(name +  " " + action + '.')
