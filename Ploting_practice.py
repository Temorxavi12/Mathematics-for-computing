import matplotlib.pyplot as plt
import math
import numpy as np
import csv

plt.xlabel('time')
plt.ylabel('speed')
plt.title('example')
FH = "C:\\Users\\xtemo\\OneDrive\\Mathematics for Computing\\Lab 1 .math\\example.txt"
x ,y = np.loadtxt('example.txt'  , delimiter = ',', unpack = True )
plt.plot(x,y ,label = 'example loaded from file')
plt.show()