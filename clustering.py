from sklearn.cluster import KMeans
import numpy as np
from lis.py import *


feature_set_3 = unigram_tfidf_normalization(dataset_clinton)
feature_set_4 = lsi(feature_set_3)

matrix = np.array(feature_set_4)
kmeans_5 = KMeans(n_clusters = 5，random_state ＝ 0).fit(matrix)
kmeans_6 = KMeans(n_clusters = 6，random_state ＝ 0).fit(matrix)
kmeans_7 = KMeans(n_clusters = 7，random_state ＝ 0).fit(matrix)
kmeans_8 = KMeans(n_clusters = 8，random_state ＝ 0).fit(matrix)
kmeans_9 = KMeans(n_clusters = 9，random_state ＝ 0).fit(matrix)
kmeans_10 = KMeans(n_clusters = 10，random_state ＝ 0).fit(matrix)

print kmeans_5