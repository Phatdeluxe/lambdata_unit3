"""
Lambdata - a collection of DS helper functions
"""
import pandas as pd
import numpy as np

#sample code

# sample datasets
ones = pd.DataFrame(np.ones(10))
zeroes = pd.DataFrame(np.zeros(50))

# sample functions
def increment(x):
    return(x + 1)

