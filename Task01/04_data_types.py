import math

# String Data Type

##Literal Asssigment##

print('')
first = 'Adam'
last = 'Noah'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

## Constructor Function##

# pizza = str('Buffalo')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

## Concatenation ## 

# fullname = first + " " + last
# print(fullname)
# fullname += '!'
# print(fullname)

## Casting a number to a string ## 
# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = 'I like The Rock from the ' + decade + 's. '
# print(statement)

## Multiple Lines ##
multiline = ''' Hey! Are you following? 
Give me a holla if you need help!!'''
# print(multiline)

## Escaping special characters ##
#sentence = 'I\'m back at work!\t Hey! \n\n Where\'s this at\\located?'
# print(sentence)


## String Methods ## 
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title()+'\n')
# print(multiline.replace('holla', 'call') + '\n')
# print(multiline)

## Print length of a string ## 
# print(len(multiline))
# multiline += '       '
# print(len(multiline))
# multiline = '    ' + multiline
# print(len(multiline))

## Strip unwanted empty characters ## 
# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))


## Build a  menu ##
# title = 'menu'.upper()
# print(title.center(20, '='))
# print("Coffee  ".ljust(16, ".") + '$2'.rjust(4))
# print("Muffin  ".ljust(16, ".") + '$3'.rjust(4))
# print("Cheesecake  ".ljust(16, ".") + '$5'.rjust(4))
# print('')

## String Index Values ##
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])

## Methods that Return Boolean Data ##
# print(first.startswith("A"))
# print(first.endswith("A"))

## Boolean Data Type ##
# myvalue = True
# x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))


## Numeric Data Type ##
# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int))

## Float Data Type ##
# gpa = 3.04
# goal_gpa = float(4.00)
# print(type(gpa))
# print(isinstance(goal_gpa, float))


## Complex Type
# complex_value = 5+3j
# print(type(complex_value))
# print(complex_value.real)
# print(complex_value.imag)

## Built-in functions for numbers
achieved_gpa = 4.28
# print(abs(achieved_gpa))
# print(round(achieved_gpa))
# print(round(achieved_gpa, 1))


## Utilizing the Math library/module
# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(achieved_gpa))
# print(math.floor(achieved_gpa))


## Casting a string to a number
zipcode = '10001'
zipcode_value= int(zipcode)
print(type(zipcode_value))






print('')

