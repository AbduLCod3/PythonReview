# Global vs Local Scope

name = 'Dave'
count = 1


def another():    
    color = 'Blue'
    global count 
    count += 1
    print(count)


    def greeting(name):
        nonlocal color
        color = 'red'
        print(color)
        print(name)
      

    greeting('Dave')

another()