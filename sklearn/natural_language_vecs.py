import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# コサイン類似度を計算する関数
def cos_sim(v1, v2):
    # np.set_printoptions(precision=3)
    similarity = np.dot(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    return similarity

# テスト用文字列
words = np.array(["しんじゅく しんじゅく", "しんじゅく じゅくじょ", "じゅくじょ はらじゅく"])
# 特徴抽出機を設置
vectorizer = TfidfVectorizer(use_idf=True, token_pattern=u"(?u)\\b\\w+\\b")
# テスト用文字列をベクトル化
vecs = vectorizer.fit_transform(words).toarray()

for i1, v1 in enumerate(vecs):
    for i2, v2 in enumerate(vecs):
        # print(v1, v2)
        print("「{}」と「{}」のコサイン類似度は{:.3f}です。".format(words[i1], words[i2], cos_sim(vecs[i1], vecs[i2])))
