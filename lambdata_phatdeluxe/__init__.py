"""
Lambdata - a collection of DS helper functions
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def split(data):
    """
    Makes a train, val, and test split from one dataframe
    """
    train, test = train_test_split(data, random_state=42, test_size=0.2)
    train, val = train_test_split(train, random_state=42, test_size=0.2)
    return train, val, test


def check_null(data):
    """
    Prints the columns with and ammounts of null values
    """
    columns = data.columns
    null_list = []
    for column in columns:
        if data[column].isnull().sum() > 0:
            null_list.append({column: data[column].isnull().sum()})
    for i in range(0, len(null_list)):
        print(null_list[i], '\n')


def add_to_df(to_series, name, df):
    """
    Takes a list and adds it to a dataframe as a new columns
    """
    new_col = pd.Series(to_series)
    df[name] = new_col
