from random import choice


# capital, bird, flower, song = ['Topeka', 'Western Meadowlark', 'Sunflower', 'Home on the Range']
capital, bird, flower, song = 'Topeka', 'Western Meadowlark', 'Sunflower', 'Home on the Range'
print(capital)
print(bird)

def random_fun_fact():
    fun_facts = ['01 Kansas has x mountains', ' 02 Instructor is from Knasas eu.' , '03 lorem-ipsum.line   Esse duis duis exercitation elit.', '04 Excepteur voluptate cillum consectetur non laborum magna incididunt eu.']

    index = choice('0123')
    print(fun_facts[int(index)])
## if we don't have this f statement, this function will be run 
## whether it is called or not as soon as it is imported in another file
## and if we call the same function, then it will run twice 
if __name__ == "__main__":
    random_fun_fact()