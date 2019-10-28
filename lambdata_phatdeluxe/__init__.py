"""
Lambdata - a collection of DS helper functions
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Function to create a train, validation, and test split
def split(data):
    train, test = train_test_split(data, random_state=42, test_size=0.2)
    train, val = train_test_split(train, random_state=42, test_size=0.2)
    return train, val, test

# Funciton to check each column in a dataframe for null values then print out a dict of the columns and their corresponding values
def check_null(data):
    columns = data.columns
    null_list = []
    for column in columns:
        if df[column].isnull().sum() > 0:
            null_list.append({column, df[column].isnull().sum()})
    for i in range(0, len(null_list)):
        print(null_list[i], '\n')

# Function to take a list, a name, and a dataframe, turn the list into a series, then add it to the dataframe with the name supplied
def add_to_df(to_series, name, df):
    new_col = pd.Series(to_series)
    df[name] = new_col

