### Modules are considered small code libraries that are based on related features

import math
from math import pi
import sys
import random as rdm
from enum import Enum
import mymodule as kansas
from RPSv5 import rock_paper_scissors

# print(math.pi)

## Find out methods inside of a module
#print(dir(rdm))

## Make it legible/readable
# for item in dir(rdm):
#     print(item)


# print(kansas.capital)
kansas.random_fun_fact()
print("\n")
# print(__name__)
# print(kansas.__name__)

# start the game 
rock_paper_scissors()