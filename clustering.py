from sklearn.cluster import KMeans
import numpy as np
from feature_generation import *

def clustering(sparse,k):
	print 'clustering...'
	kmeans = KMeans(n_clusters = k).fit(sparse)
	return kmeans.labels_

if __name__ == '__main__':
	dataset = dataset_clinton
	feature_set_1 = unigram_feature(dataset)
	s = words2sparse(feature_set_1)
	print clustering(s,5)
