from common import *
from feature_generation import unigram_tfidf_normalization
from scipy.sparse import coo_matrix
from sklearn.decomposition import TruncatedSVD

def lsi(dataset):
	mat = []
	wordDic = dict()
	row,col,data = [],[],[]
	for index in range(0,len(dataset)):
		for token,value in dataset[index][1]:
			if not (token in wordDic):
				wordDic[token] = len(wordDic)
			row += [index]
			col += [wordDic[token]]
			data += [value]
	sparse_matrix = coo_matrix((data, (row, col)), shape=(len(dataset), len(wordDic))).toarray()
	print len(wordDic)
	return sparse_matrix

if __name__ == '__main__':
	feature_set_3 = unigram_tfidf_normalization(dataset_clinton)
	feature_set_4 = lsi(feature_set_3)
