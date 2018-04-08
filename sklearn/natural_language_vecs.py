import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def cos_sim(v1, v2):
    similarity = np.dot(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))
    return similarity

np.set_printoptions(precision=3)
words = np.array(["しんじゅく しんじゅく", "しんじゅく じゅくじょ", "じゅくじょ はらじゅく"])

words

vectorizer = TfidfVectorizer(use_idf=True, token_pattern="(?u)\\b\\w+\\b")
vecs = vectorizer.fit_transform(words)
vecs = (vecs.toarray())
vecs

for i1, v1 in enumerate(vecs):
    for i2, v2 in enumerate(vecs):
        print("「" + words[i1] + "」 と 「" + words[i2] + "」 のコサイン類似度は" + "%1.3F" % cos_sim(vecs[i1], vecs[i2]) + "です。")
