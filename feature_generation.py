from common import *
from nltk.tokenize import TweetTokenizer
from nltk import pos_tag
from math import log
from nltk.corpus import stopwords
from nltk.stem.porter import *

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

def tfidf(tokenized_dataset):
	ret = []
	idf = dict()
	# idf pass
	print "start idf pass"
	n_document = 0
	for row in tokenized_dataset:
		n_document += 1
		tokens = row[1]
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
		idf[key] = log(1.0*n_document/value)
	# tf pass
	print "start tf pass"
	total = 0

	n_document = 0
	n_empty = 0
	for row in tokenized_dataset:
		n_document += 1
		tokens = row[1]
		tf = dict()
		for token in tokens:
			if token in tf:
				tf[token] += 1
			else:
				tf[token] = 1
		selected = []
		n_tokens = len(tokens)

		for token,freq in tf.items():
			vtfidf = freq*idf[token]/n_tokens
			selected += [(token,vtfidf)]
		ret += [row[0], selected]
	return ret

def unigram_tfidf(filename):
	print "loaindg TweetTokenizer..."
	tknzr = TweetTokenizer()
	ret = []

	# tokenize
	print "start tokenizing"
	tokenized_dataset = []
	with open(preprocessed_filename(filename), 'rb') as csvfile:
		reader = csv_reader(csvfile)
		for row in reader:
			text = row[1]
			tokens = tknzr.tokenize(text)
			tokenized_dataset += [[row[0],tokens]]
	
	ret = tfidf(tokenized_dataset)
	
	return ret

def unigram_tfidf_normalization(filename):

	tknzr = TweetTokenizer()
	stopword = set(stopwords.words('english'))
	stemmer = PorterStemmer()

	def normalize(text):
		ret = []
		tokens = tknzr.tokenize(text)
		tags = pos_tag(tokens)
		for token,tag in tags:
			token = ''.join([i for i in token if i.isalpha()])
			token = token.lower()
			if tag in ['NNP','NNPS']:
				continue
			if token in stopword:
				continue
			token = stemmer.stem(token)
			ret += [token]
		return ret
	print "start tokenizing"
	tokenized_dataset = []
	with open(preprocessed_filename(filename), 'rb') as csvfile:
		reader = csv_reader(csvfile)
		for row in reader:
			text = row[1]
			tokens = normalize(text)
			tokenized_dataset += [[row[0],tokens]]
	
	ret = tfidf(tokenized_dataset)

	return []


if __name__ == '__main__':
	unigram_tfidf_normalization(dataset_clinton)
	# unigram_tfidf(dataset_clinton,0.5)