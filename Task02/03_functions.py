def hello_world():
    print("")
    print('Hello World!')
    
hello_world()



# def sum(num1=0, num2=0):
#     # check our input
#     if (type(num1) is not int or type(num2) is not int):
#         return 0
#     return (num1 + num2)

# total = sum(2, 3)
# total = sum('x', 3)
# total= sum()
# print(total)



## How to handle if you don't know 
## the number of arguments that your function will receive

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", 1, True)

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = 'Dave', last ="Gray")









print("")
