import numpy as np
import math
import random
from particle import Particle

def cost(pos):
    x = pos[0]
    y = pos[1]
    #this is the cost function and can be anything
    return (1.5-x)**2 + 100.*(y-x**2)**2


#The algorithm
#X(t+1) = X(t) + V(t+1)
#V(t+1) = wV(t) + r1*c1*(P - X(t)) + r1*c2*(G-X(t))


w = 0.9
c1 = 2
c2 = 2
bounds = ([-3,3],[-3,3])
globalBestPosition = np.array([random.uniform(bounds[0][0],bounds[0][1]),random.uniform(bounds[1][0],bounds[1][1])])
globalBestVal = cost(globalBestPosition)
numParticles = 1000
numIterations = 300
error =  globalBestVal
particles = []
for x in range(numParticles):
    particles.append(Particle(bounds,cost))

for y in range(numIterations):
    for particle in particles:
        returnValues = particle.evaluate(bounds,cost, w, c1 , c2, globalBestPosition)
        if(returnValues[0] < globalBestVal): #at this point we've got a new global best
            globalBestVal = returnValues[0]
            globalBestPosition = returnValues[1]
            error = globalBestVal
        print(error)
    w = w- 0.01
print(w)
print(globalBestPosition)