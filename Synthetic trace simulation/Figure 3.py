import numpy as np
import random
import matplotlib.pyplot as plt

bt = np.load('btcos30.npy')
for i in range(30):
    bt[i]-= 49.8
x_axis = np.arange(1,31)

plt.bar(x_axis, bt, color = 'darkorange', width = 0.5, bottom = 49.8, zorder=3)

plt.yticks(np.arange(50,60,2))
plt.grid(zorder = 0)
plt.xlabel('Frame',fontsize=18)
plt.ylabel('Optimal $B^*_k$',fontsize=18)

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
f = plt.figure(num = 1)
f.set_figwidth(7)
f.set_figheight(5)
f.savefig('optimalBkbar.pdf', dpi = 1400, format = 'pdf')

