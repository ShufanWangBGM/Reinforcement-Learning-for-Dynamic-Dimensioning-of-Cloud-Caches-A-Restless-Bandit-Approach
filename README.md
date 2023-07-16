# Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach
This repository contains the code used in evaluating the IEEE INFOCOM 2022 paper titled "Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach". 

## General Description
The synthetic trace and real trace based simulations for index-based policies (when the system parameters are known) are run as follows:
1. Generate the synthetic traces in which the requests in each time frame follow the Zipf distribution.
2. Obtain the optimal cache dimensioning in each time frame using a fluid analysis model. In particular, we use [Gurobi](https://www.gurobi.com) as the LP solver.
3. Compute Whittle indices for each content.
4. Excute the fluid Whittle index policy.

## Figure Description
### Figures using synthetic trace
1. Preparation: We generate the request probablity matrix for N = 100 contents in K = 30 frames. The Zipf parameter is set to 0.6 for all frames. A more detailed description can be found in the paper. The request matrix is saved as Requestmatrixsamealpha.npy.
2. Number of requests plot: This shows the bar plot of requests using the probability matrix (see Figure2.py).
3. Fluid analysis: This solves the optimal cache dimensioning in each frame using fluid analysis (see fluidmodel.py).
4. Optimal cache dimensioning plot: This shows the bar plot of optimal cache dimensioning from fluid analysis (see Figure3.py).
5. Compute Whittle indices: Given the transition probability matrix, we directly calculate the Whittle index via the closed-from expressions (17) in the paper (see calculatewhittle.py).
6. Draw cost figures using different policies including Random, LRU, f-Whittle and fW-UCB algorithm (see Figure4.py).
### Figures using real trace
1. We use two publicly avaiable CDN traces to evaluate our policies.
2. Optimal cache dimensioning plot: This solves optimal cache dimensioning in each frame using fluid analysis (see optimal.py).
3. Calculate Whittle indice for each content in the trace (see whittle.py).

If you have any questions, feel free to reach out to us (swang214@binghamton.edu).

# Reference
Any academic work, which is built on this code, should use reference of the following paper.
>Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach\
>Guojun Xiong, Shufan Wang, Gang Yan, Jian Li\
>IEEE INFOCOM 2022
>
>Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach\
>Guojun Xiong, Shufan Wang, Gang Yan, Jian Li\
>IEEE/ACM Transactions on Networking (TON), to appear, 2023
