#Doing this test to remind myself how numpy arrays work
import numpy as np

pos = np.array([1, 2])
#this is a scalar multiple 
print(3*pos)
#see what happens when add or subtract
#needs to be elementwise 
print(pos+np.array([1.5,15]))



#######################################
#Test to see if you can pass a function
#######################################

def calculateZ(pos):
    return pos[0] + pos[1] + 5

def evaluate(position, function):
    return function(position)


print("------------------------------")
p = [1,3]
print(p)
print(evaluate(p,calculateZ))