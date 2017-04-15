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

More information to be updated soon.
