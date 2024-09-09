import os
# RAWX is similar to CRUD

## RAWX
# R = Read    
# A = Append 
# W = Write  
# X = Create  

## CRUD
# C = Create    
# R = Read 
# U = Update  
# D = Delete 

### Read - error if file doesn't exit
f = open("names.txt", 'r')

## Reads the entire file
# print(f.read()) 

## Reads the first 3 characters
# print(f.read(3)) 

## Reads the first line of the file
#print(f.readline()) 

for line in f:
    print(line)

# It is important to close the file
# updates/chanes only applied when file is closed
f.close()

try:
    f = open("name_list.txt")
    print(f.read())

except:
    print('File Doesn\'t Exist.')

finally:
    f.close()


# Append - creates the file if it doesn't exist
# f = open("names.txt", "a")
# f.write("Neil\n")
# f.close()


# f = open("names.txt")
# print(f.read())
# f.close()



# Write - Creates a new file, if the file if it does't exist
# Write - OverWrites the file if it does exist
f = open("context.txt", "w")
f.write("I deleted all names in the context file.\n")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Delete - Deletes a file 

# Check if a file does exist before attempting to create it
if not os.path.exists("dave.txt"):
    f = open("dave.txt", 'x')
    f.close()

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete doesn't exist.")


# a more consie way to handle file opening error
with open('more_names.txt') as f:
    content = f.read()

with open("names.txt", 'w') as f:
    f.write(content)