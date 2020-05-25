
##################################################################################################################
"""

"""

# Built-in/Generic Imports

# Libs
import matplotlib.pyplot as plt

# Own modules
from RSAI_Engine.Environment.RSAI_environment import RSAI_environment
from RSAI_Engine.Agent.RSAI_agent import Agent

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '26/04/2020'

##################################################################################################################

env = RSAI_environment()
agent_dict = {"Bob": Agent("Bob", (10, 10))}

print(env.shape)

env.visualise_environment("Dev test run", agent_dict, press_start=False)
