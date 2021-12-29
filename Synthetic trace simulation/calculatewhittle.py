import numpy as np
import random
import matplotlib.pyplot as plt
import math
import heapq

def cost_cal(s,l):
    reward = s/l
    return reward

def average(lst):
    return sum(lst)/len(lst)
pop  = np.load('popcos30.npy')
bt = np.load('btcos30.npy')
lambda1=30
lambda2=20
d1 = 40
d2 = 40
p1 = lambda1/d1
p2 = lambda2/d2
q = 0.9
n_content = 100
state_max = 10
for i in range(n_content):
    W = np.zeros((state_max +1,n_content))
    
    Ecost = np.zeros((state_max +1,n_content))



    
Iteration=1000
T=100

s1 = []
s2 = []
for i in range(T+1):
    s1.append(0)
    s2.append(0)

C1 = []
C2 = []
for i in range(Iteration + 2):
    C1.append(0)
    C2.append(0)

for n in range(n_content):
    for threshold in range(state_max + 1):
        for index in range(1, Iteration + 2):
            if index == 1:
                s1[1] = 5
                s2[1] = 5
            else:
                s1[1] = s1[T]
                s2[1] = s2[T]
            for i in range(2,T+1):
                if s1[i] < threshold:
                    temp = random.uniform(0,1)
                    if temp <= p1:
                        s1[i] = s1[i-1] +1
                    else:
                        s1[i] = s1[i-1]
                else:
                    temp1 = random.uniform(0,1)
                    if temp1 <= q:
                        s1[i] = 0
                    elif temp1 >= 1 - (1-q) * p1:
                        s1[i] = s1[i-1] + 1
                    else:
                        s1[i] = s1[i-1]
                        
                
                if s2[i] < threshold:
                    temp = random.uniform(0,1)
                    if temp <= p1:
                        s2[i] = s2[i-1] +1
                    else:
                        s2[i] = s2[i-1]
                else:
                    temp1 = random.uniform(0,1)
                    if temp1 <= q:
                        s2[i] = 0
                    elif temp1 >= 1 - (1-q) * p2:
                        s2[i] = s2[i-1] + 1
                    else:
                        s2[i] = s2[i-1]
                C1[index][n] = C1[index][n] + cost_cal(s1[i-1],lambda1)
                C2[index][n] = C2[index][n] + cost_cal(s2[i-1],lambda2)
            
        Ecost[threshold] = average(C1)
        Ecost[threshold] = average(C2)
for n in range(n_content):    
    for i in range(1,state_max+1):
        W[i][n] = Ecost[i]-Ecost[i-1]

np.save(W, 'whittleindex.npy')
