import random
import numpy as np
import matplotlib.pyplot as plt
alpha = np.zeros(30)
for i in range(30):
    alpha[i] = 60
alpha /= 100
print(alpha)
'''
Answer = 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6
 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6 0.6
'''
n_frame = 30
n_content = 100
ratio = np.zeros(n_frame)
S_max = 10
pop = np.zeros((n_frame, n_content))
for j in range(n_frame):
    sum_ial = 0
    
    for i in range(1,n_content+1):
        sum_ial += 1/(i**alpha[j])
    Aa = 1/sum_ial
    for i in range(n_content):
        pop[j][i] = Aa/((i+1)**alpha[j])
for j in range(n_frame):
    ratio[j] = 1
    pop[j] *= ratio[j]
print(ratio)
pop1 = np.zeros((n_frame, n_content))
request_ratio = [1, 2, 4, 10, 5, 3, 0.1, 1, 0.8, 1.3, 2, 1.1, 0.8, 6, 8, 13, 15, 14, 10, 8, 4, 2, 1.5, 1.2, 8, 4.6, 5, 2, 1, 1.5]
for j in range(n_frame):
    pop1[j] = random.sample(list(pop[j]), len(pop[j])) 
    pop1[j] *= request_ratio[j]
print(pop1)
np.save('Requestmatrixsamealpha.npy', pop1)
