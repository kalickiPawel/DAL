import pandas as pd
import numpy as np

from scipy.io import arff

if __name__ == "__main__":
    '''
        Zadanie 1
    '''
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
    print(f'Ilosc elementów o wartosciach spoza przedzialu [−2,2]: {df[(df < -2) | (df > 2)].count().sum()}')
    # 1.b
    print(f'Ilosc elementów o wartościach spoza przedziału [−2,2] w każdej kolumnie:\n{df[(df < -2) | (df > 2)].count()}')
    # 1.c
    print(df.applymap(lambda x: None if x < -2 or x > 2 else x).dropna())
    # 1.d
    print(df.applymap(lambda x: x**2 if x < 0 else x))

    '''
        Zadanie 2
    '''
    filename = '../data/soybean.arff'
    data, meta = arff.loadarff(filename)
    df1 = pd.DataFrame(data).select_dtypes([np.object]).stack().str.decode('utf-8').unstack()
    print(f'Probek w pliku: {df1.shape[0]}')
    # 2.a
    print(f"Próbek z brakujace wartosci: {df1.shape[0] - df1[df1 != '?'].dropna().shape[0]}")
    # 2.b
    print(f"Lista ilosci brakujacych wartosci:\n{np.vstack((np.unique((df1 == '?').sum(axis=1), return_counts=True)))}")
    # 2.c
    c = df1[df1 == '?'].count()
    print(f'Ile kolumn z brakujacymi wartosciami:\n{c[c >= 1].count()}')
    print(f"Kolumny gdzie występują brakujące wartości:\n{c[c >= 1]}")
