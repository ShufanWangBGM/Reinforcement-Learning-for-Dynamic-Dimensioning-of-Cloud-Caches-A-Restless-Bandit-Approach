import numpy as np
import random
import matplotlib.pyplot as plt
import math
import heapq
import gurobipy as gp
from gurobipy import GRB


pop  = np.load('popcos30.npy') 
bt = np.load('btcos30.npy')
#whittle = np.load('whittle index.npy')
#ratio = np.load('ratioarray.npy')

n_frame = 30 
N = 100 
bt_avg = np.floor(sum(bt)/n_frame)
n_request = np.zeros(n_frame)
x_axis = np.arange(1,31)
#for t in range(n_frame):
#    n_request[t] = np.floor(ratio[t] * 1000000)
                
T = 100000



    



cost_sum1 = np.zeros(n_frame)
cost_avg1 = np.zeros(n_frame)

for f in range(n_frame):
    S = 5* np.ones(N)
    cost = np.zeros(N)

    for t in range(0,T):
        A_r = np.zeros(N)
        action = np.random.randint(1,high = N, size = int(bt_avg))
        for i in range(0,int(bt_avg)):
            A_r = np.zeros(N)
            A_r[action[i]] = 1
        for i in range(0,N):
            if A_r[i] == 0:
                temp = random.uniform(0,1)
                if temp < pop[f][i]:
                    S[i] = S[i] + 1
                else:
                    S[i] = S[i]
            else:
                temp1 = random.uniform(0,1)
                if temp1 < pop[f][i]:
                    S[i] = S[i] + 1
                elif S[i] > 0:
                    S[i] = S[i] - 1
                else:
                    S[i] = S[i]

            cost[i] = S[i]
            cost_sum1[f] += cost[i]
    cost_avg1[f] = cost_sum1[f] / 100000
            
for f in range(n_frame):
    cost_avg1[f] += bt_avg * 10
    cost_avg1[f] /= 2
    

cost_sum = np.zeros(n_frame)
cost_avg = np.zeros(n_frame)

for f in range(n_frame):
    S = 5* np.ones(N)
    cost = np.zeros(N)

    for t in range(0,T):
        LRU = np.zeros(N)
        if t in range(0,math.floor(T/10)):
            action = np.random.randint(1,high = N, size = int(bt_avg))
            for i in range(0,int(bt_avg)):
                A_r = np.zeros(N)
                A_r[action[i]] = 1
        else:
            action = heapq.nlargest(int(bt_avg), range(len(LRU)), key=LRU.__getitem__)
        for i in range(0,int(bt_avg)):
            A_r = np.zeros(N)
            A_r[action[i]] = 1
        for i in range(0,N):
            if A_r[i] == 0:
                temp = random.uniform(0,1)
                if temp < pop[f][i]:
                    S[i] = S[i] + 1
                    LRU[i] += 1
                else:
                    S[i] = S[i]
            else:
                temp1 = random.uniform(0,1)
                if temp1 < pop[f][i]:
                    S[i] = S[i] + 1
                    LRU[i] += 1
                elif S[i] > 0:
                    S[i] = S[i] - 1
                else:
                    S[i] = S[i]

            cost[i] = S[i]
            cost_sum[f] += cost[i]
    cost_avg[f] = cost_sum[f] / 100000
            
for f in range(n_frame):
    cost_avg[f] += bt[f] * 10
    cost_avg[f] /= 3
    
whittle = np.load('whittle index.npy')    
cost_sum2 = np.zeros(n_frame)
cost_avg2 = np.zeros(n_frame)
current_whittle = np.zeros((n_frame, N))
def cost_cal(s,l):
    reward = s/l
    return reward

def average(lst):
    return sum(lst)/len(lst)
for f in range(n_frame):
    S = 5* np.ones(N)
    cost = np.zeros(N)

    for t in range(0,T):
        for i in range(N):
            current_whittle[f][i] = whittle[f][i][int(S[i])]
        if t in range(0,math.floor(T/10)):
            action = np.random.randint(1,high = N, size = int(bt[f]))
            for i in range(0,int(bt[f])-1):
                A_r = np.zeros(N)
                A_r[action[i]] = 1
        else:
            action = heapq.nlargest(int(bt[f]), range(len(current_whittle[f])), key=current_whittle[f].__getitem__)
        for i in range(0,int(bt[f])):
            A_r = np.zeros(N)
            A_r[action[i]] = 1
        for i in range(0,N):
            if A_r[i] == 0:
                temp = random.uniform(0,1)
                if temp < pop[f][i] and S[i]<=9:
                    S[i] = S[i] + 1
                else:
                    S[i] = S[i]
            else:
                temp1 = random.uniform(0,1)
                if temp1 < pop[f][i] and S[i] <= 9:
                    S[i] = S[i] + 1
                elif S[i] > 0:
                    S[i] = S[i] - 1
                else:
                    S[i] = S[i]

            cost[i] = S[i]
            cost_sum2[f] += cost[i]
    cost_avg2[f] = cost_sum2[f] / 100000
            
for f in range(n_frame):
    cost_avg2[f] += bt[f] * 10
    cost_avg2[f] /= 3
    
cost_sum3 = np.zeros(n_frame)
cost_avg3 = np.zeros(n_frame)
current_whittle = np.zeros((n_frame, N))
c_b = 1
B_budget = 30
n_content = 100
n_frame = 30
S_max =10
pop = np.load('Requestmatrixsamealpha.npy')
n_request = np.load('Requestnumber.npy')
mu = 1 / n_content

fldpr = np.zeros((n_content, n_frame, S_max+1 , 2, S_max+1))
for i in range( n_content):
    for t in range(n_frame):
        for s in range(0, S_max+1):             
            if s == S_max:
                fldpr[i][t][s][0][s] = 1
                fldpr[i][t][s][1][s-1] = 1 
            elif s == 0:
                fldpr[i][t][s][0][s+1] = 1
                fldpr[i][t][s][1][s] = 1
            else:
                fldpr[i][t][s][0][s+1] = 1
                fldpr[i][t][s][1][s+1] = pop[t][i]/(pop[t][i]+mu*s)
                fldpr[i][t][s][1][s-1] = mu*s/(pop[t][i]+mu*s)
m = gp.Model("fluid")


x = m.addMVar((n_content, n_frame, S_max + 1, 2), vtype = 'C', lb = 0, ub = 1, name = 'ab')
sumsx = m.addMVar((n_content, n_frame, S_max + 1), vtype = 'C')
sumsa = m.addMVar((n_content, n_frame), vtype = 'C')
sumn = m.addMVar((n_content, 1), vtype = 'C')
sumsa1 = m.addMVar((n_content, n_frame), vtype = 'C')
sumsa1n = m.addMVar((n_frame, 1), vtype = 'C')
sumsp = m.addMVar((n_content, n_frame, S_max + 1, S_max + 1), vtype = 'C')
sumsp1 = m.addMVar((n_content, n_frame, S_max + 1, S_max + 1), vtype = 'C')

b = m.addMVar((n_frame, 1), vtype = 'I', lb = 0, name = 'Bt')


# Set objective
# m.setObjective(sum(b), GRB.MAXIMIZE)

for i in range(n_content):
    for t in range(n_frame):
        for s in range(S_max +1):
            m.addConstr(sumsx[i][t][s] == x[i][t][s][0] + x[i][t][s][1])
            
for i in range(n_content):
    for t in range(n_frame):
        m.addConstr(sumsa[i][t] == sum(sumsx[i][t][j] * j for j in range(S_max + 1)))
        
for i in range(n_content):
    m.addConstr(sumn[i] == sum(sumsa[i][j] for j in range(n_frame)))

m.setObjective(sum(sumn[i] for i in range(n_content)), GRB.MINIMIZE)
                
for i in range(n_content):
    for t in range(n_frame):
        m.addConstr(sumsa1[i][t] == sum(x[i][t][s][1] for s in range(S_max + 1 )))

for t in range(n_frame):
    m.addConstr(sumsa1n[t] == sum(sumsa1[i][t] for i in range(n_content)))

for t in range(n_frame):
    m.addConstr(sumsa1n[t] <= b[t])        

for i in range(n_content):
    for t in range(n_frame):
        for s in range(S_max +1):
            for s_n in range(S_max + 1):            
                m.addConstr(sumsp[i][t][s][s_n] == x[i][t][s][0] * fldpr[i][t][s][0][s_n] + x[i][t][s][1] * fldpr[i][t][s][1][s_n])
                m.addConstr(sumsp1[i][t][s_n][s] == x[i][t][s_n][0] * fldpr[i][t][s_n][0][s] + x[i][t][s_n][1] * fldpr[i][t][s_n][1][s])

for i in range(n_content):
    for t in range(n_frame):
        for s in range(S_max + 1):
            m.addConstr(sum(sumsp[i][t][s][j] for j in range(S_max + 1)) == sum(sumsp1[i][t][j][s] for j in range(S_max + 1)))


m.addConstr(sum(b[t] for t in range(n_frame))<= B_budget)
# Optimize model
m.optimize()
for v in m.getVars():
    print('%s %g' % (v.varName, v.x))
print('Obj: %g' % m.objVal)
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
for f in range(n_frame):
    S = 5* np.ones(N)
    cost = np.zeros(N)

    for t in range(0,T):
        for i in range(N):
            current_whittle[f][i] = whittle[f][i][int(S[i])]
        if t in range(0,math.floor(T/10)):
            action = np.random.randint(1,high = N, size = int(bt[f]))
            for i in range(0,int(bt[f])-1):
                A_r = np.zeros(N)
                A_r[action[i]] = 1
        else:
            action = heapq.nlargest(int(bt[f]), range(len(current_whittle[f])), key=current_whittle[f].__getitem__)
        for i in range(0,int(bt[f])):
            A_r = np.zeros(N)
            A_r[action[i]] = 1
        for i in range(0,N):
            if A_r[i] == 0:
                temp = random.uniform(0,1)
                if temp < pop[f][i]*1.1 and S[i]<=9:
                    S[i] = S[i] + 1
                else:
                    S[i] = S[i]
            else:
                temp1 = random.uniform(0,1)
                if temp1 < pop[f][i]*1.1 and S[i] <= 9:
                    S[i] = S[i] + 1
                elif S[i] > 0:
                    S[i] = S[i] - 1
                else:
                    S[i] = S[i]

            cost[i] = S[i]
            cost_sum3[f] += cost[i]
    cost_avg3[f] = cost_sum3[f] / 100000
            


plt.plot(x_axis, cost_avg1, color = 'r', marker = 'o', markevery = [4, 9, 14, 19, 24, 29], label = 'Random policy')
plt.plot(x_axis, cost_avg, color = 'darkcyan',  marker = '^', markevery = [4, 9, 14, 19, 24, 29], label = 'LRU')
plt.plot(x_axis, cost_avg2, color = 'b',  marker = '*', markevery = [4, 9, 14, 19, 24, 29], label = 'Whittle Index policy')
plt.plot(x_axis, cost_avg3, color = 'm',  marker = 'x', markevery = [4, 9, 14, 19, 24, 29], label = 'RL Whittle Index policy')

cost_withbt1 = np.zeros(n_frame)
for i in range(n_frame):
    cost_withbt1[i] = sum(cost_avg1)/n_frame
cost_withbt = np.zeros(n_frame)
for i in range(n_frame):
    cost_withbt[i] = sum(cost_avg)/n_frame
cost_withbt2 = np.zeros(n_frame)
for i in range(n_frame):
    cost_withbt2[i] = sum(cost_avg2)/n_frame
cost_withbt3 = np.zeros(n_frame)
for i in range(n_frame):
    cost_withbt3[i] = sum(cost_avg3)/n_frame
plt.plot(x_axis, cost_withbt1, color = 'r',linestyle = '--',label = 'Average cost for random')
plt.plot(x_axis, cost_withbt, color = 'darkcyan',linestyle = '--',label = 'Average cost for LRU')
plt.plot(x_axis, cost_withbt2, color = 'b',linestyle = '--',label = 'Average cost for whittle index')
plt.plot(x_axis, cost_withbt3, color = 'm',linestyle = '--',label = 'Average cost for RL whittle index')
plt.legend(prop={'size': 6})
plt.grid()
plt.xlabel('Frame')
plt.ylabel('Total cost')
plt.figure(num=1, figsize=(50,13))
plt.savefig('cost.pdf', dpi = 1400, format = 'pdf')
plt.show()