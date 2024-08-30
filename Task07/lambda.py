from functools import reduce

# Lambda a function a single expression that returns a single value
squared = lambda num : num * num # notice we are not using return
print(squared(2))

addTwo = lambda num: num + 2
print(addTwo(12))


sum_total = lambda a, b : a + b
print(sum_total(10, 8))


##########################################################
# Use lambda function when you don't need its result save for use later
def functionBuilder(x):
    return lambda num : num + x

addTen = functionBuilder(10)
addTwenty = functionBuilder(20)

print(addTen(7))
print(addTwenty(7))

######################################################
numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)
print(list(squared_nums))

######################################################
odd_nums=  filter(lambda num : num % 2 != 0, numbers)
print(list(odd_nums))

######################################################
total = reduce(lambda acc, curr : acc + curr, numbers)
print(total, 10)
print(sum(numbers))

#####################################################
names = ['Abdul Rahman', 'Sara Ito', 'John Jacob jingleheimerschmidt']
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)

## Remember a higher function is a function that recieves another function or returns another function