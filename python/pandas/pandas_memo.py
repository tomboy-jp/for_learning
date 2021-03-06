import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# numpyから作る場合
df = pd.DataFrame(np.random.rand(10, 5))

# colmun指定
df.columns = ["A", "B", "C", "D", "E"]

# "A"列についての情報を出力
print(df["A"].describe())

# "A"が0.4以上かつ"B"が0.9以下の行だけを抽出
df = df[(df["A"] >= 0.4) & (df["B"] <= 0.9)]

# indexの連番振り直し
df = df.reset_index(drop=True)

# dfオブジェクトのforループの廻し方
for index, row in df.iterrows():
    print(index, row["B"])

# pandasでグラフを描画
df.plot(y=["A","B","C","D","E"], colormap='cool', marker='.', markersize=10, title='DataFrameTest', figsize=(10,5), alpha=0.5)
plt.pause(10)
