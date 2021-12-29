import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gurobipy as gp
from gurobipy import GRB

def load_mats():
    Path = ""
    Mats = []
    with open(Path) as fr:
        for f in fr:
            data = f[:-1].split(" ")
            gdata = []
            for d in data:
                gdata.append(float(d))
            Mats.append(np.array(gdata))

    return Mats

pop1 = load_mats()
L = len(pop1)

b_show = np.zeros(L)
obj = np.zeros(L)
for frame in range(L):
    pop = pop1[frame]
    kapa = 0.5
    #n_frame = 30
    n_content = len(pop1[frame])
    S_max = 10
    c_b = 10
    # B_budget = 30
    # n_request = np.load('Requestnumber.npy')
    mu = 0.1


    fldpr = np.zeros((n_content, S_max + 1, 2, S_max + 1))
    for i in range(n_content):
        for s in range(0, S_max + 1):
            if s == S_max:
                fldpr[i][s][0][s] = 1
                fldpr[i][s][1][s - 1] = 1
            elif s == 0:
                fldpr[i][s][0][s + 1] = 1
                fldpr[i][s][1][s] = 1
            else:
                fldpr[i][s][0][s + 1] = 1
                fldpr[i][s][1][s + 1] = pop[i] / (pop[i] + mu * s)
                fldpr[i][s][1][s - 1] = mu * s / (pop[i] + mu * s)

    m = gp.Model("fluid")
    m.params.NonConvex = 2

    x = m.addMVar((n_content, S_max + 1, 2), vtype='C', lb=0, ub=1, name='ab')
    sumsx = m.addMVar((n_content, S_max + 1), vtype='C', name='sumsx')
    sumsa = m.addMVar((n_content), vtype='C', name='sumsa')

    sumsa1 = m.addMVar((n_content, 1), vtype='C', name='sumsa1')
    # sumsa1n = m.addMVar((n_frame, 1), vtype = 'C')
    sumsp = m.addMVar((n_content, S_max + 1, S_max + 1), vtype='C', name='sumsp')
    sumsp1 = m.addMVar((n_content, S_max + 1, S_max + 1), vtype='C', name='sumsp1')

    b = m.addMVar(1, vtype='I', lb=0, name='B')

    # Set objective
    # m.setObjective(sum(b), GRB.MAXIMIZE)

    for i in range(n_content):
        for s in range(S_max + 1):
            m.addConstr(sumsx[i][s] == x[i][s][0] + x[i][s][1])

    for i in range(n_content):
        m.addConstr(sumsa[i] == sum(sumsx[i][j] * j for j in range(S_max + 1)))

    for i in range(n_content):
        m.addConstr(sum(sumsx[i][j] for j in range(S_max + 1)) == 1)

    m.setObjective(kapa * sum(sumsa[i] for i in range(n_content)) + (1 - kapa) * c_b * b, GRB.MINIMIZE)

    for i in range(n_content):
        m.addConstr(sumsa1[i] == sum(x[i][s][1] for s in range(S_max + 1)))

    m.addConstr(sum(sumsa1[i] for i in range(n_content)) <= b, name='ineq1')

    for i in range(n_content):
        for s in range(S_max + 1):
            for s_n in range(S_max + 1):
                m.addConstr(sumsp[i][s][s_n] == x[i][s][0] * fldpr[i][s][0][s_n] + x[i][s][1] * fldpr[i][s][1][s_n])
                m.addConstr(
                    sumsp1[i][s_n][s] == x[i][s_n][0] * fldpr[i][s_n][0][s] + x[i][s_n][1] * fldpr[i][s_n][1][s])

    for i in range(n_content):
        for s in range(S_max + 1):
            m.addConstr(sum(sumsp[i][s][j] for j in range(S_max + 1)) == sum(sumsp1[i][j][s] for j in range(S_max + 1)))

    # m.addConstr(sum(b[t] for t in range(n_frame))<= B_budget)

    # Optimize model
    m.optimize()

    v = m.getVars()
    b_opt = v[-1]
    b_show[frame] = b_opt.x
    obj[frame] = m.objVal

plt.plot(b_show)
plt.show()

plt.plot(obj)
plt.show()

