# This module is playing around different functions of Pandas lib
# Follows PEP-8 standard. Author: Ram. Created on July 27, 2018 6:15 AM

import pandas as pd
import numpy as np


def func1Series():
    """
    This deals with pandas.Series. Just playing around
    """

    s = pd.Series(np.array(['a', 'b', 'c']), index=[100, 101, 102])
    s1 = pd.Series([1,2,3], index=['a', 'b', 'c'])
    try:
        #print(s.append('12'))  # cannot append to a series, bcoz its just a dataframe object for 1D array
        print(s)
        print("Any data type can be kept as index in 1D array ie. Series", s1)
        print("s1", s[10])
    except Exception as e:
        print("exception:", e)

def func2CSV():
    """
    This method is just playing around CSV read, write, update functions in pandas
    :return: None
    """


if __name__ == "__main__":
    filename = "sample.csv"
    func1Series()
    func2CSV()
