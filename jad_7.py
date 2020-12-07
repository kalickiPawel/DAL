import pandas as pd
import numpy as np
from itertools import combinations

from scipy.io import arff

if __name__ == "__main__":
    # Exercise 1.
    filename = './data/weather.arff'
    data, meta = arff.loadarff(filename)

    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(data).select_dtypes([np.object]).stack().str.decode('utf-8').unstack()

    df1 = df1.drop(columns=df2.select_dtypes([np.object]).columns)
    df = df2.join(df1)
    # Exercise 2.
    df = df.dropna()
    df = df[df != "?"].dropna()

    # print(df.head())
    # print(df.columns)
    # print(f'Probek w pliku: {df.shape[0]}')
    # Exercise 3.
    for col in df1:
        df[col] = pd.cut(
            df[col].values,
            [0, int(np.mean([min(df[col].values), max(df[col].values)])), max(df[col].values)]
        ).codes
    for col in df2:
        classes = np.unique(df[col])
        df[col] = [np.where(classes == weather)[0][0] for weather in df[col]]

    print(df)

    # Exercise 4. & 5.

    lst = ['temperature', 'humidity', 'windy', 'play']
    rs_max = 0
    df_new = df

    while rs_max != 1.0:
        df_nconf = df_new.drop_duplicates(subset=lst, keep=False)  # niesprzeczne

        gamma_all = len(df_nconf) / len(df_new)
        print(f"Gamma dla wszystkich: {gamma_all}")

        df_nconf_list = [df_new.drop_duplicates(subset=list(x), keep=False) for x in combinations(lst, len(lst) - 1)]

        gammas = [len(el) / len(df) for el in df_nconf_list]
        for i, gamma in enumerate(gammas):
            print(f"Gamma {lst[i]}: {gamma}")

        rs = [(gamma_all - gamma) / gamma_all for gamma in gammas]
        for i, r in enumerate(rs):
            print(f"R {lst[i]}: {r}")

        df_new = df.drop([lst[min(range(len(rs)), key=rs.__getitem__)]], axis=1)
        lst.remove(lst[min(range(len(rs)), key=rs.__getitem__)])
        print(lst)
        rs_max = max(rs)

    print(f"-----\nRedukt: {lst}")

    # Exercise 6.

    df_pewne = df.drop_duplicates()  # -> if not duplicates
    # print(df.duplicated().value_counts())
    # print(df)
    # df_sprzeczne = 0 # -> if duplicates.num ??
    # df_niepewne = 0 # -> if duplicates.num ??

    # -- Ideas -- #
    # df2 = df.drop(["windy"], axis=1)
    # df_nconf2 = df2.drop_duplicates(subset=['temperature', 'humidity', 'play'], keep=False)  # niesprzeczne
    # gamma_all2 = len(df_nconf2) / len(df2)
    # print(f"Gamma dla wszystkich: {gamma_all2}")
    #
    # lst2 = ['temperature', 'humidity', 'play']
    #
    # df_nconf_list2 = [df2.drop_duplicates(subset=list(x), keep=False) for x in combinations(lst2, len(lst2) - 1)]
    # gammas2 = [len(el) / len(df2) for el in df_nconf_list2]
    # for i, gamma in enumerate(gammas2):
    #     print(f"Gamma x{i}: {gamma}")
    # print()
    # rs2 = [(gamma_all - gamma) / gamma_all for gamma in gammas2]
    # for i, r in enumerate(rs2):
    #     print(f"R x{i}: {r}")
    #
    # df3 = df2.drop(["play"], axis=1)
    # df_nconf3 = df3.drop_duplicates(subset=['temperature', 'humidity'], keep=False)  # niesprzeczne
    # gamma_all3 = len(df_nconf3) / len(df3)
    # print(f"Gamma dla wszystkich: {gamma_all3}")
    #
    # lst3 = ['temperature', 'humidity']
    #
    # df_nconf_list3 = [df3.drop_duplicates(subset=list(x), keep=False) for x in combinations(lst3, len(lst3) - 1)]
    # gammas3 = [len(el) / len(df3) for el in df_nconf_list3]
    # for i, gamma in enumerate(gammas3):
    #     print(f"Gamma x{i}: {gamma}")
    # print()
    # rs3 = [(gamma_all - gamma) / gamma_all for gamma in gammas3]
    # for i, r in enumerate(rs3):
    #     print(f"R x{i}: {r}")

    # data_frame_1 = 0 # -> sprzeczne -> if duplicates.num ??
    # data_frame_2 = 0 # -> niepewne -> if duplicates.num ??
    # data_frame_3 = 0 # -> pewne -> if not duplicates
