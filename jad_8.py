import pandas as pd
import matplotlib.pyplot as plt

from scipy.io import arff

if __name__ == "__main__":
    # Zadanie 1.
    filename = './data/stock.arff'
    data, meta = arff.loadarff(filename)
    df = pd.DataFrame(data)
    # Zadanie 2.
    df['date'] = pd.date_range(start='1/1/1988', periods=len(df), freq='D')
    df1 = df.set_index(['date'])
    print(df1)

    # Zadanie 3.
    for column in df1.columns:
        if column != 'date':
            df1[column] = pd.to_numeric(df1[column], downcast='float')

    for index, row in df1.iterrows():
        for column in df1.columns:
            if column != 'date':
                df1[column][index] = row[column] / 100

    df1.plot()
    plt.show()

    # Zadanie 4.
    df2 = df.rolling(100, min_periods=1).mean()
    df2.plot()
    plt.show()
