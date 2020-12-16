import pandas as pd
import numpy as np
import os

from scipy.io import arff
from src.utils import get_project_root

root = get_project_root()


class SixthLab:
    def __init__(self):
        self.exercise_01()
        self.exercise_02()

    @staticmethod
    def exercise_01():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 1~~~~~~~~~~~~~~~~~~~~")
        n_bar, n_sd, n = 0, 1, 1000
        df = pd.DataFrame(
            dict(
                a=np.random.normal(loc=n_bar, scale=n_sd, size=n),
                b=np.random.normal(loc=n_bar, scale=n_sd, size=n),
                c=np.random.normal(loc=n_bar, scale=n_sd, size=n),
                d=np.random.normal(loc=n_bar, scale=n_sd, size=n)
            ),
            columns=['a', 'b', 'c', 'd']
        )
        # print(df)
        # 1.a
        print("Number of items with values out of the range [−2,2]: {}".format(
            df[(df < -2) | (df > 2)].count().sum()))
        # 1.b
        print("Number of items with values out of the range [−2,2] in each of column:\n{}".format(
              df[(df < -2) | (df > 2)].count()))
        # 1.c
        print(df.applymap(lambda x: None if x < -2 or x > 2 else x).dropna())
        # 1.d
        print(df.applymap(lambda x: x ** 2 if x < 0 else x))

    @staticmethod
    def exercise_02():
        print("~~~~~~~~~~~~~~~~~~~~~~~Exercise 2~~~~~~~~~~~~~~~~~~~~")
        filename = os.path.join(root, os.path.join('data', 'soybean.arff'))
        data, meta = arff.loadarff(filename)
        df1 = pd.DataFrame(data).select_dtypes([np.object]).stack().str.decode('utf-8').unstack()
        print(f"Samples in the file: {df1.shape[0]}")
        # 2.a
        print(f"Samples with missing values: {df1.shape[0] - df1[df1 != '?'].dropna().shape[0]}")
        # 2.b
        print("List of quantities of missing values:\n{}".format(
            np.vstack((np.unique((df1 == '?').sum(axis=1), return_counts=True)))))
        # 2.c
        c = df1[df1 == '?'].count()
        print(f"How many columns with missing values are there:\n{c[c >= 1].count()}")
        print(f"Columns with missing values:\n{c[c >= 1]}")
