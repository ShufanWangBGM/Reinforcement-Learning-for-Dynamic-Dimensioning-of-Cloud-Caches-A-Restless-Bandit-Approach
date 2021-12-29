# Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach
This is the code for our work "Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach" accepted by INFOCOM 2022.
## General description
The steps for synthetic and real trace are shown as following:\
1, (Synthetic trace only) Generate the probablity distribution (Zipf distribution) of the request contents.\
2, Use fluid analysis to achieve the optimal cache capacity in each frame. We use [Gurobi](https://www.gurobi.com) as the LP solver. Note full knowledge of transition probabilities is required.\
3, Calculate the whittle index table for all contents.\
4, Excute policies.
## Figure description
### Figures using synthetic trace
Preparation: we generate the request probablity matrix for N = 100 contents in K = 30 frames. The Zipf distritbuion parameter is set to 0.6 for all frames. The request matrix will be saved as Requestmatrixsamealpha.npy.\
Figure 2: shows the bar plot of requests using the probability matrix. As shown in Figure2.py.\
Fluid analysis: solve optimal cache capacity in each frame using fluid analysis. The optimal capacity for 30 frames will be saved as btcos30.npy. As shown in fluidmodel.py.\

### Figures using real trace
Figure 1 shows a different setting of \gamma which gives a different performance in Algorithm 2 and 3.\
Figure 2,3,4,5 show a wider range of \lambda and \gamma for biased error for Algorithm 2 and 3.\
Figure 6 shows different performance for different \lambda using Algorithm 4.\
Figure 7 shows different performance for different number of predictions using Algorithm 4.\
Figure 8,9 show the impact of biased error using Algorithm 4.\
Figure 10,11 show the performance of multi-prediction, multi-shop randomized algorithm( Algorithm 5).\
Figure 12 shows the performance of Algorithm 4 with real-world dataset.
# Reference
Any academic work, which is built on this code, should use reference of the following paper.
> Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach\
> Guojun Xiong, Shufan Wang, Gang Yan, Jian Li\
> INFOCOM 2022
