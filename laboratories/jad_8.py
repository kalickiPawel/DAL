import os
import pandas as pd
import matplotlib.pyplot as plt

from scipy.io import arff
from src.utils import get_project_root

root = get_project_root()


class EighthLab:
    filename = ''
    df = None

    def __init__(self):
        self.exercise_01()
        df = self.exercise_02()
        print(df)
        self.exercise_03(df)

    def exercise_01(self):
        self.filename = os.path.join(root, os.path.join('data', 'stock.arff'))
        data, meta = arff.loadarff(self.filename)
        self.df = pd.DataFrame(data)

    def exercise_02(self):
        self.df['date'] = pd.date_range(start='1/1/1988', periods=len(self.df), freq='D')
        return self.df.set_index(['date'])

    @staticmethod
    def exercise_03(df):
        for column in df.columns:
            if column != 'date':
                df[column] = pd.to_numeric(df[column], downcast='float')

        for index, row in df.iterrows():
            for column in df.columns:
                if column != 'date':
                    df[column][index] = row[column] / 100

        df.plot()
        plt.show()

    def exercise_04(self):
        df = self.df.rolling(100, min_periods=1).mean()
        df.plot()
        plt.show()
