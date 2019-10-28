"""
Lambdata - a collection of DS helper functions
"""
import pandas as pd
import numpy as np

#sample code

# sample datasets
ONES = pd.DataFrame(np.ones(10))
ZEROES = pd.DataFrame(np.zeros(50))

# sample functions
def increment(x):
    return(x + 1)

