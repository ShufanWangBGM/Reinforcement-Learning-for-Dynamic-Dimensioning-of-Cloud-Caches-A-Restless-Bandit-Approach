# Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach
This is the code for our work "Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach" accepted by IEEE INFOCOM 2022. 
## General description
The steps for synthetic and real trace are shown as following:\
1, (Synthetic trace only) Generate the probablity distribution (Zipf distribution) of the request contents.\
2, Use fluid analysis to achieve the optimal cache capacity in each frame. We use [Gurobi](https://www.gurobi.com) as the LP solver. Note full knowledge of transition probabilities is required.\
3, Calculate the whittle index table for all contents.\
4, Excute policies.\
If you have any questions, feel free to ask me (swang214@binghamton.edu).
## Figure description
### Figures using synthetic trace
1, Preparation: we generate the request probablity matrix for N = 100 contents in K = 30 frames. The Zipf distritbuion parameter is set to 0.6 for all frames. A more detailed description can be found in our paper. The request matrix will be saved as Requestmatrixsamealpha.npy.\
2, Number of requests plot: shows the bar plot of requests using the probability matrix. As shown in Figure2.py.\
3, Fluid analysis: solve optimal cache capacity in each frame using fluid analysis. The optimal capacity for 30 frames will be calculated. As shown in fluidmodel.py.\
4, Optimal Bt plot: shows the bar plot of optimal Bt from fluid analysis. As shown in Figure3.py.\
5, Calculate whittle index for f-Whittle: given the transition probability matrix, we can directly calculate the whittle index via the closed form (17) in the paper. As in calculatewhittle.py.\
6, Draw cost figures using different policies. Here we use random, LRU, f-Whittle and fW-UCB algorithms. A more detailed explanation can be found in our paper. As in Figure4.py.
### Figures using real trace
1, A more detailed explanation on the real trace dateset we chose can be found in our paper.\
2, Optimal Bt plot: solve optimal cache capacity in each frame using fluid analysis. The optimal capacity for 28 frames will be calculated. As shown in optimal.py.\
3, Calculate whittle index for the trace. As shown in whittle.py.
# Reference
Any academic work, which is built on this code, should use reference of the following paper.
url: "https://github.com/github/linguist"
preferred-citation:
  type: article
  authors:
  - family-names: "Lisa"
    given-names: "Mona"
    orcid: "https://orcid.org/0000-0000-0000-0000"
  - family-names: "Bot"
    given-names: "Hew"
    orcid: "https://orcid.org/0000-0000-0000-0000"
  doi: "10.0000/00000"
  journal: "Journal Title"
  month: 9
  start: 1 # First page number
  end: 10 # Last page number
  title: "My awesome research software"
  issue: 1
  volume: 1
  year: 2021
@inproceedings{xiong2022reinforcement,
  title={Reinforcement Learning for Dynamic Dimensioning of Cloud Caches: A Restless Bandit Approach},
  author={Xiong, Guojun and Wang, Shufan and Yan, Gang and Li, Jian},
  booktitle={Proc. of IEEE INFOCOM},
  year={2022}
}
