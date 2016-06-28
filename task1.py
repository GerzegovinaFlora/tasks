import random
import math
import sys


a=[1,5,-65,7,3]

def myMax(massiv):
    b=massiv[0]
    for x in range(0,len(massiv)):
        if massiv[x]<b:
            b=massiv[x]
    return b


print(myMax(a))


# превратить в стрингу и обрезать
# max число
# nod
# sort
