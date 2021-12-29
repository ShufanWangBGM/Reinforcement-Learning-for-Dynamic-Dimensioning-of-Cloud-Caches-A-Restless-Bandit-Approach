# Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach
This is the code for our work "Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach" accepted by INFOCOM 2022.
## General description
The steps for synthetic and real trace are shown as following:
1, (Synthetic trace only) Generate the probablity distribution (Zipf distribution) of the request contents.
2, Use fluid analysis to achieve the optimal cache capacity in each frame. We use [Gurobi](https://www.gurobi.com) as the LP solver. Note full knowledge of transition probabilities is required.
3, Calculate the whittle index table for all contents.
4, Excute policies.
## Figure description
### Figures using synthetic trace
Figure 1 shows the performance of single prediction, multi-shop deterministic algorithm( Algorithm 2).\
Figure 2 shows the performance of single prediction, multi-ship randomized algorithm( Algorithm 3).\
Figure 3 shows the possible outperformance of Algorithm 2 over Algorithm 3.\
Figure 4 shows the impact of \lambda.\
Figure 5 shows the impact of biased errors for both Algorithm 2 and 3.\
Figure 6 gives a real-world dateset to simulate the performance of Algorithm 2, compared with pure online algorithm without predictions.\
Figure 7 shows the performance of multi-prediction, multi-shop deterministic algorithm( Algorithm 4).
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
