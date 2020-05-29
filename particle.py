import numpy as np
import random
import math
#the particle class needs to have the following
#Current position (x and y coordinate)
#Velocity the vector in which the particle will move in the next iteration
#The best position it has seen (the x and y coordinates)
#The value at the best position so this can be compared

#We need a search space 
class Particle:
    def __init__(self, bounds, costFunc):
        #the initial position which we will randomly choose
        initialx = random.uniform(bounds[0][0],bounds[0][1]) #finding a uniform value between the lower and upper bounds of the x value
        initialy = random.uniform(bounds[1][0],bounds[1][1]) #finding a uniform value between the lower and upper bounds of the y value
        self.position = np.array([initialx,initialy])
        #the velocity vector randomized
        self.velocity = np.array([random.uniform(-1,1),random.uniform(-1,1)])
        #The best position
        self.bestPostion=self.position
        #The best cost 
        self.bestCost = costFunc(self.position)
    
    #X(t+1) = X(t) + V(t+1)
    #V(t+1) = wV(t) + r1*c1*(P - X(t)) + r1*c2*(G-X(t))
    #there is a lot of paramaters here might want to clean this shit up at some point
    def evaluate(self, bounds,costFunction, w, c1 , c2, globalBestPosition):
        r1 = random.uniform(-1,1)
        r2 = random.uniform(-1,1)
        v = w*self.velocity + r1 * c1 *(self.bestPostion - self.position) + r2 * c2 * (globalBestPosition - self.position)
        x = self.position + v
        #now we have the new position so we need to do some checks
        lowerX = bounds[0][0]
        upperX = bounds[0][1]
        lowerY = bounds[1][0]
        upperY = bounds[1][1]
        if x[0] < lowerX:
            x[0] = lowerX
            v[0] = -v[0]
        if x[0] > upperX:
            x[0] = upperX
            v[0] = -v[0]
        if x[1] < lowerY:
            x[1] = lowerY
            v[1] = -v[1]
        if x[1] > upperY:
            x[1] = upperY
            v[1] = -v[1]
        self.position = x
        newCost = costFunction(x)
        if newCost < self.bestCost:
            self.bestCost = newCost
            self.bestPostion = x
        return [newCost,self.position]
