import numpy as np
import random
import matplotlib.pyplot as plt
import math
import heapq


def calculatewhittle(pop):
    n_frame = len(pop)
    S_max = 10
    Ite = 100

    wit = []
    cst = []
    Ecst = []
    state = []
    a = []

    for i in range(len(pop)):
        lmax = len(pop[i])

        wit0 = np.zeros((1, lmax, S_max + 1))
        cst0 = np.zeros((1, lmax, S_max + 1, Ite))
        Ecst0 = np.zeros((1, lmax, S_max + 1))
        state0 = np.zeros((1, lmax, 100))
        a0 = np.zeros((1, lmax))

        wit.append(wit0[0])
        cst.append(cst0[0])
        Ecst.append(Ecst0[0])
        state.append(state0[0])
        a.append(a0[0])

    for t in range(n_frame):
        n_content = len(pop[t])
        mu = 1 / n_content
        print(n_frame,n_content,mu)

        for thre in range(S_max + 1):
            for it in range(Ite):
                if it == 0:
                    for i in range(n_content):
                        state[t][i][0] = 5
                else:
                    state[t][i][0] = state[t][i][99]

                for tau in range(1, 100):
                    for i in range(n_content):
                        if state[t][i][tau - 1] < thre:
                            a[t][i] = 0
                            state[t][i][tau] = state[t][i][tau - 1] + 1
                        else:
                            a[t][i] = 1
                            temp = random.uniform(0, 1)
                            if temp < pop[t][i] / (pop[t][i] + mu * state[t][i][tau - 1]) and state[t][i][
                                tau - 1] < S_max:
                                state[t][i][tau] = state[t][i][tau - 1] + 1
                            else:
                                state[t][i][tau] = state[t][i][tau - 1] - 1
                        cst[t][i][thre][it] += state[t][i][tau - 1]
            for i in range(n_content):
                Ecst[t][i][thre] = sum(cst[t][i][thre]) / 100
            for i in range(n_content):
                if thre == 0:
                    wit[t][i][thre] = Ecst[t][i][thre]
                else:
                    wit[t][i][thre] = Ecst[t][i][thre] - Ecst[t][i][thre - 1]

        print(wit[t])

    return wit



def get_whittle(pop):
    S_max = 10
    Ite = 100

    n_content = len(pop[0])
    mu = 1 / n_content

    LMax = n_content
    wit = np.zeros((1, LMax, S_max + 1))
    cst = np.zeros((1, LMax, S_max + 1, Ite))
    Ecst = np.zeros((1, LMax, S_max + 1))
    state = np.zeros((1, LMax, 100))
    a = np.zeros((1, LMax))

    t = 0

    for thre in range(S_max + 1):
        print("step ",thre+1)
        for it in range(Ite):
            if it == 0:
                for i in range(n_content):
                    state[t][i][0] = 5
            else:
                #for i in range(n_content):
                    state[t][i][0] = state[t][i][99]

            for tau in range(1, 100):
                for i in range(n_content):
                    if state[t][i][tau - 1] < thre:
                        a[t][i] = 0
                        state[t][i][tau] = state[t][i][tau - 1] + 1
                    else:
                        a[t][i] = 1
                        temp = random.uniform(0, 1)
                        if temp < pop[t][i] / (pop[t][i] + mu * state[t][i][tau - 1]) and state[t][i][
                            tau - 1] < S_max:
                            state[t][i][tau] = state[t][i][tau - 1] + 1
                        else:
                            state[t][i][tau] = state[t][i][tau - 1] - 1
                    cst[t][i][thre][it] += state[t][i][tau - 1]
        for i in range(n_content):
            Ecst[t][i][thre] = sum(cst[t][i][thre]) / 100
        for i in range(n_content):
            if thre == 0:
                wit[t][i][thre] = Ecst[t][i][thre]
            else:
                wit[t][i][thre] = Ecst[t][i][thre] - Ecst[t][i][thre - 1]

    print(len(wit),len(wit[0]))
    return wit


def load_pops(F,Hour):
    H = Hour * 3600
    Pops = []
    Path = r"C:\Users\forev\Desktop\Redis-资料\Results\Mats\ReqMat_" + str(F) + "_" + str(H) + ".txt"
    with open(Path) as fr:
        for f in fr:
            data = f[:-1].split(" ")
            gdata = []
            for d in data:
                gdata.append(float(d))
            Pops.append(gdata)

    return Pops

if __name__ == '__main__':
    Pops = load_pops(50,6)
    #calculatewhittle(Pops)
    for pop in Pops:
        print("Get...")
        Wit = get_whittle([pop])
        print(Wit)





