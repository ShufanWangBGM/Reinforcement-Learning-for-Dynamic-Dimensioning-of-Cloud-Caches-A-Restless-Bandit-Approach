import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gurobipy as gp
from gurobipy import GRB


n_frame = 30
n_content = 100
S_max = 10
c_b = 1
B_budget = 30
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
