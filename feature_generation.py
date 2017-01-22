from common import *
from nltk.tokenize import TweetTokenizer
from math import log

def unigram_feature(filename):
	tknzr = TweetTokenizer()
	# wordDic = dict()
	ret = []
	with open(preprocessed_filename(filename), 'rb') as csvfile:
		reader = csv_reader(csvfile)
		for row in reader:
			text = row[1]
			tokens = tknzr.tokenize(text)
			ret+=[[row[0],' '.join(tokens)]]
			# for token in tokens:
			# 	if token in wordDic:
			# 		continue
			# 	wordDic[token] = len(wordDic)
	return ret

def unigram_tfidf(filename, threshold):
	idf = dict()
	tknzr = TweetTokenizer()
	# idf pass
	with open(preprocessed_filename(filename), 'rb') as csvfile:
		reader = csv_reader(csvfile)
		n_document = 0
		for row in reader:
			n_document += 1
			text = row[1]
			tokens = tknzr.tokenize(text)
			document_set = set()
			for token in tokens:
				if token in document_set:
					continue
				document_set.add(token)
				if token in idf:
					idf[token] += 1
				else:
					idf[token] = 1
		for key,value in idf.items():
			idf[key] = log(1.0*value/n_document)
	# tf pass
	with open(preprocessed_filename(filename), 'rb') as csvfile:
		reader = csv_reader(csvfile)
		n_document = 0
		for row in reader:
			
	return []

def unigram_tfidf_normalization(filename, threshold):
	return []


if __name__ == '__main__':
	unigram_tfidf(dataset_clinton,0)