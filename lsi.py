from common import *
from feature_generation import unigram_tfidf_normalization
from scipy.sparse import coo_matrix
from sklearn.decomposition import TruncatedSVD
from sklearn.utils.extmath import randomized_svd

def lsi(dataset, n_topic):
	mat = []
	wordDic = dict()
	row,col,data = [],[],[]
	# build sparse matrix
	for index in range(0,len(dataset)):
		for token,value in dataset[index][1]:
			if not (token in wordDic):
				wordDic[token] = len(wordDic)
			row += [index]
			col += [wordDic[token]]
			data += [value]
	sparse_matrix = coo_matrix((data, (row, col)), shape=(len(dataset), len(wordDic))).toarray()
	# U, Sigma, VT = randomized_svd(sparse_matrix, n_components=n_topic,
 #                                      n_iter=5,
 #                                      random_state=None)
	# return U
	svd = TruncatedSVD(n_components=n_topic)
	u = svd.fit_transform(sparse_matrix)
	print svd.explained_variance_
	return u

if __name__ == '__main__':
	feature_set_3 = unigram_tfidf_normalization(dataset_test)
	feature_set_4 = lsi(feature_set_3)
