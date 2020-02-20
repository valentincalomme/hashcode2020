#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('cd', '../src')


# In[2]:


import os

from problem import Problem

problems = {}

folder = "../data/problems"

for filename in os.listdir(folder):
    
    problems[filename[0]] = Problem(name=filename[0], filename=os.path.join(folder, filename))


# In[3]:


from solvers.random_solver import RandomSolver
from solvers.greedy_solver import GreedySolver
from solvers.raw_potential_solver import RawPotentialSolver

# solver = RandomSolver()
# solver = RawPotentialSolver()
solver = GreedySolver()


# In[4]:


for name, problem in problems.items():
    
    for i, solution in enumerate(solver.yield_solutions(problem)):
        print(solution.to_file())
        break

