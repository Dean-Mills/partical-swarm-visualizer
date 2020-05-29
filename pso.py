import numpy as np
import math

def cost(pos):
    x = pos[0]
    y = pos[1]
    #this is the cost function and can be anything
    return (1.-x)**2 + 100.*(y-x**2)**2


#The algorithm
#X(t+1) = X(t) + V(t+1)
#V(t+1) = wV(t) + r1*c1*(P - X(t)) + r1*c2*(G-X(t))


w = 0.9
c1 = 2
c2 = 2
bounds = ([-2,2],[-2,2])
globalBestPosition = np.array(random.uniform(bounds[0][0],bounds[0][1]),random.uniform(bounds[1][0],bounds[1][1])])
globalBestVal = cost(globalBestPosition)
numParticles = 300
numIterations = 100
error = 100 #Guess this can be anything

a = 3
if a > 5.0:
    print("Works as expected")
