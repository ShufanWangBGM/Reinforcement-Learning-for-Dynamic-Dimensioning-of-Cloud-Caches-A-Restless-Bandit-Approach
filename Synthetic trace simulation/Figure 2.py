import gurobipy as gp
from gurobipy import GRB

import numpy as np
import random
import matplotlib.pyplot as plt
import math
import heapq
'''
def mystep(x,y, ax=None, where='pre', **kwargs):
    assert where in ['post', 'pre']
    x = np.array(x)
    y = np.array(y)
    if where=='post': y_slice = y[:-1]
    if where=='pre': y_slice = y[1:]
    X = np.c_[x[:-1],x[1:],x[1:]]
    Y = np.c_[y_slice, y_slice, np.zeros_like(x[:-1])*np.nan]
    if not ax: ax=plt.gca()
    return ax.plot(X.flatten(), Y.flatten(), **kwargs)
'''
pop = np.load('Requestmatrixsamealpha.npy')

n_frame = 30
n_content = 100
n_request = np.zeros(n_frame)
for j in range(n_frame):
    n_request[j] = sum(pop[j]) * 1000000 
x_axis = np.arange(1,n_frame + 1)

plt.bar(x_axis, n_request, color="maroon", width = 0.5 , zorder=3)
plt.yticks(np.arange(0,2500000,500000))
plt.ylim(top = 2300000)
plt.grid(zorder = 0)
plt.xlabel('Frame',fontsize=18)
plt.ylabel('Total number of requests',fontsize=18)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

fig, ax = plt.subplots()
ax.yaxis.offsetText.set_fontsize(1)

f = plt.figure(num = 1)
f.set_figwidth(7)
f.set_figheight(5)
f.savefig('totalrequestbar.pdf', dpi = 1400, format = 'pdf')


