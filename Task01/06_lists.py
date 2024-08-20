

### Various types of lists ###
users = ['Son', 'John', 'adam']
data = ['Abdul', 32, True]
empty_list = []

## Check if a value is inside a list ##
# print('Dave' in empty_list)

## print a value in a specific position ##
# print(users[0])
# print(data[-1])

## Find the position of a specific value ##
# print(users.index('Adam'))

## print a range of values ##
# print(users[0:2])
# print(users[1:])
# print(users[0:])
# print(users[-3:-1])

## print the length of a list ##
# print(len(data))

## append/add a value(s) to a list ##
users.append('Elsa')
print(users)
# users += ['Jason']
# print(users)
# users.extend(['Robert', 'Ali', 'Noah'])
# print(users)
# users.extend(data)
# print(users)

## Add/append/insert a value into a list in a specific position ##
users.insert(0, 'Bob')
print(users)
users[2:2] = ['Eddie', 'Alex']
print(users)
users [1:5] = ['JPJ', 'Robert']
print(users)

## Remove items for a list
users.remove('Bob')
print(users)

## Remove last item of  a list
users.pop()
print(users)

## Remvove an item on a specific poistion
# del users[0]
# print(users)

## you can delete the entire the list ##
# del data

## Clear the contents of a list
data.clear()
print(data) 

## Sort a list
users.sort()
print(users)

## Sort a list in alphabetical order 
## Accounts for both lowercase and uppercase starts.
## Works only on a list of the same data type(strings).
# users.sort(key=str.lower)
# print(users)

# nums = [4, 42, 78, 1, 5]
# print(nums)
# nums.reverse()
# print(nums)

## This sorts in ascending order
# nums.sort(reverse=True)
# print(nums)

## Returns a sorted list without altering the original.
# print(sorted(nums, reverse=True))

## Create a copy of a list
# nums_copy = nums.copy()
# # Using list constructor to create a new list
# my_nums = list(nums)
# my_copy = nums [:]
# my_copy.sort()
# print(nums_copy)
# print(my_nums)
# print(my_copy)
# print(type(nums))


## Tuples
## creating a tuple with constructor
my_tuple = tuple(('Dave', 23, True))

## creating a tuple WITHOUT constructor
mytuple2 = (1, 2, 3, 4, 5, 2, 2)
print(type(my_tuple))

# One way to modify a tuple is:
## 1st: Copy a tuple into a new list using the list() constructor.
new_list = list(my_tuple)
## 2nd: Modify the list, in this case adding another value
new_list.append('24.5')
## 3rd: Create a new tuple from the list using the tuple() constructor.
new_tuple = tuple(new_list)
print('Original Tuple:', my_tuple)
print('New Tuple:', new_tuple)


## Unpacking 

(name, age, *the_rest) = new_tuple
print(name)
print(age)
print(the_rest)

## count the # of occurances of a value in a tuple
print(mytuple2.count(2))