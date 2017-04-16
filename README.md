# Understanding Norm Change: An Evolutionary Game-Theoretic Approach
by Soham De, Dana S Nau, Michele J Gelfand (University of Maryland)

Source code in Python for running simulations of the model presented in the following paper: [link](http://www.gelfand.umd.edu/papers/De%20Nau%20Gelfand%20Norm%20Change%20AAMAS.pdf). The paper appears in the Proceedings of the 2017 International Conference on Autonomous Agents & Multiagent Systems (AAMAS), and an extended version will be available soon on arXiv.

This README goes through the functionalities of each file in the source code. The code has been tested with Python version 2.7.8.

---

There are two different settings in the paper:
1. Infinite well-mixed population using the replicator dynamic. Code for this is under the `well_mixed` folder.
2. Structured population (we consider a grid in the paper) with the evolutionary dynamic defined by the Fermi rule. Code for this is under the `structured` folder.

---

Under the folder `well_mixed`, there are two files:
1. `replicator.py`: Norm change on an infinite well-mixed population using the replicator dynamic [Figure 4 and 5 in paper].
2. `mutator_replicator.py`: Norm change on an infinite well-mixed population using the replicator-mutator dynamic [Figure 7 in paper].

Both these files can be simply run as `python replicator.py` or `python mutator_replicator.py`, with specific settings set inside each file.

---

Under the folder `structured`, there are two main files `main.py` and `main_explore.py`. `main.py` runs the norm change experiments with one structural shock [Figure 6 in the paper]. `main_explore.py` runs the experiments studying the evolution of exploration rates [Figure 8 in the paper]. Both files can be run as follows:

```
python main.py/main_explore.py {a} {b} {network_type} {network_params} {run_no} {c}
```

`a` and `b` denote the payoffs of the game matrix used.

`network_type` denotes the type of network to be used. `globals.py` contains the various types of networks supported. We used a `grid` network for our experiments.

`network_params` denotes the parameters of the network type. For a `grid` network, it should contain the rows and columns of the grid, separated by a comma, without spaces. For example, for a `grid` network of 20 rows and 30 columns, we would denote `network_params` as `20,30`.

`run_no` denotes a unique identifier for that particular run.

`c` denotes the need for coordination in the game matrix.



