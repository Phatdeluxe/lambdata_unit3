"""
utility functions for working with DataFrames
"""

import pandas as pd
from sklearn.model_selection import train_test_split


class Data:
    """
    For use with dataframes and the many things you want to do to them
    """
    def __init__(self, df):
        self.df = df

    def check_null(self):
        """
        Prints the columns with and ammounts of null values
        """
        columns = self.df.columns
        null_list = []
        for column in columns:
            if self.df[column].isnull().sum() > 0:
                null_list.append({column: self.df[column].isnull().sum()})
        for i in range(0, len(null_list)):
            print(null_list[i], '\n')

    def split(self):
        """
        Makes a train, val, and test split from one dataframe
        """
        train, test = train_test_split(self.df, random_state=42, test_size=0.2)
        train, val = train_test_split(train, random_state=42, test_size=0.2)
        return train, val, test


def add_to_df(to_series, name, df):
    """
    Takes a list and adds it to a dataframe as a new columns
    """
    new_col = pd.Series(to_series)
    df[name] = new_col
