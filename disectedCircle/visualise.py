#This script is to try visulaise the problem.
import matplotlib.pyplot as plt
import numpy as np
from random import random

n=4 #Set n

def point():
    #Generates a random point on the circle
    theta = random() * 2 * np.pi
    return np.cos(theta), np.sin(theta)

#Generate random points
randomPoint_1=point()
randomPoint_2=point()
randomPoint_3=point()
randomPoint_4=point()

#Generate points on circle
theta = np.linspace(0, 2*np.pi, 100)
r = np.sqrt(1.0)

#Generate Circle
x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

#Rename random points
x3 = (randomPoint_1[0],randomPoint_1[1])
x4 = (randomPoint_2[0],randomPoint_2[1])
x5 = (randomPoint_3[0],randomPoint_3[1])
x6 = (randomPoint_4[0],randomPoint_4[1])

fig, ax = plt.subplots(1)

#Plot Circle
ax.plot(x1, x2) 

#Plot random Points
ax.plot(x3[0],x3[1],marker='o',color='red')
ax.plot(x4[0],x4[1],marker='o',color='red')
ax.plot(x5[0],x5[1],marker='o',color='red')
ax.plot(x6[0],x6[1],marker='o',color='red')

#Plot lines conecting random points
ax.plot([x3[0],x4[0],x5[0],x6[0]],[x3[1],x4[1],x5[1],x6[1]])

ax.set_aspect(1)

plt.show()