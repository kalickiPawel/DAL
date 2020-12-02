import pandas as pd
import numpy as np
from itertools import combinations

from scipy.io import arff

if __name__ == "__main__":
    # 1.
    filename = './data/weather.arff'
    data, meta = arff.loadarff(filename)

    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(data).select_dtypes([np.object]).stack().str.decode('utf-8').unstack()

    df1 = df1.drop(columns=df2.select_dtypes([np.object]).columns)
    df = df2.join(df1)

    df = df.dropna()
    df = df[df != "?"].dropna()

    # print(df.head())
    # print(df.columns)
    # print(f'Probek w pliku: {df.shape[0]}')

    for col in df1:
        df[col] = pd.cut(
            df[col].values,
            [0, int(np.mean([min(df[col].values), max(df[col].values)])), max(df[col].values)]
        ).codes
    for col in df2:
        classes = np.unique(df[col])
        df[col] = [np.where(classes == weather)[0][0] for weather in df[col]]

    print(df)

    df_nconf = df.drop_duplicates(subset=['temperature', 'humidity', 'windy', 'play'], keep=False) # niesprzeczne
    gamma_all = len(df_nconf) / len(df)
    print(f"Gamma dla wszystkich: {gamma_all}")

    lst = ['temperature', 'humidity', 'windy', 'play']

    df_nconf_list = [df.drop_duplicates(subset=list(x), keep=False) for x in combinations(lst, len(lst)-1)]
    gammas = [len(el)/len(df) for el in df_nconf_list]
    for i, gamma in enumerate(gammas):
        print(f"Gamma x{i}: {gamma}")
    print()
    rs = [(gamma_all - gamma) / gamma_all for gamma in gammas]
    for i, r in enumerate(rs):
        print(f"R x{i}: {r}")

    # data_frame_1 = 0
    # data_frame_2 = 0
    # data_frame_3 = 0
