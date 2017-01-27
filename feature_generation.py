from common import *
from nltk.tokenize import TweetTokenizer
from nltk import pos_tag
from math import log
from nltk.corpus import stopwords
from nltk.stem.porter import *
from scipy.sparse import coo_matrix
from CMUTweetTagger import *

def unigram_feature(filename):
	tknzr = TweetTokenizer()
	# wordDic = dict()
	ret = []
	with open(preprocessed_filename(filename), 'rb') as csvfile:
		reader = csv_reader(csvfile)
		for row in reader:
			text = row[1]
			tokens = tknzr.tokenize(text)
			freq = dict()
			for token in tokens:
				if token in freq:
					freq[token] += 1
				else:
					freq[token] = 1
			features = [(token,value) for token,value in freq.items()]
			ret+=[[row[0],features]]
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
			total += 1
		ret += [[row[0], selected]]
		if len(selected) == 0:
			n_empty += 1
	print "Avg. length of vectors: "+str(1.0*total/n_document)
	print "# of empty vectors: "+str(n_empty)
	print "# of words: " + str(len(idf))
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
	success = check_script_is_present()
	if not success:
		print 'Error: CMU Tweet Tagger is absent.'
		exit(-1)

	stopword = set(stopwords.words('english'))
	stemmer = PorterStemmer()
	def normalize(tokens):
		ret = []
		for token,tag,v in tokens:
			if tag == '^':
				continue
			token = ''.join([i for i in token if i.isalpha()])
			if len(token) == 0:
				continue
			token = token.lower()
			if token in stopword:
				continue
			token = stemmer.stem(token)
			ret += [token]
		return ret
	print "start tokenizing"
	tokenized_dataset = []
	n_document = 0
	sentences = []
	tweet_ids = []
	with open(preprocessed_filename(filename), 'rb') as csvfile:
		reader = csv_reader(csvfile)
		for row in reader:
			tweet_ids += [row[0]]
			text = row[1]
			sentences += [text]
	sentences = runtagger_parse(sentences)
	for index in range(0,len(sentences)):
		tokens = normalize(sentences[index])
		tokenized_dataset += [[tweet_ids[index],tokens]]
		n_document += 1
		if n_document%10000 == 0:
			print str(n_document) +" documents tokenized"
	ret = tfidf(tokenized_dataset)
	return ret

def words2vector(dataset):
	ret = []
	wordDic = dict()
	for row in dataset:
		tweet_id = row[0]
		words = row[1]
		for key,value in words:
			if not (key in wordDic):
				wordDic[key] = len(wordDic)
	for row in dataset:
		tweet_id = row[0]
		words = row[1]
		vector = [0 for i in range(0,len(wordDic))]
		for key,value in words:
			vector[wordDic[key]] = value
		ret += [[tweet_id,vector]]
	return ret

def words2sparse(dataset):
	wordDic = dict()
	rows,cols,data = [],[],[]
	for index in range(0,len(dataset)):
		row = dataset[index]
		tweet_id = row[0]
		words = row[1]
		for key,value in words:
			if not (key in wordDic):
				wordDic[key] = len(wordDic)
			rows += [index]
			cols += [wordDic[key]]
			data += [value]
	sparse_matrix = coo_matrix((data, (rows, cols)), shape=(len(dataset), len(wordDic)))
	return sparse_matrix

if __name__ == '__main__':
	dataset = dataset_test
	feature_set_1 = unigram_tfidf_normalization(dataset)
	s = words2sparse(feature_set_1)
	# print len(feature_set_1)
	# feature_set_2 = unigram_tfidf(dataset)
	# print len(feature_set_2)
	# feature_set_3 = unigram_tfidf_normalization(dataset)
	# print len(feature_set_3)
	# with open(result_filename(dataset),'wb') as outfile:
	# 	writer = csv_writer(outfile)
	# 	writer.writerow(['tweet id','feature set 1','feature set 2','feature set 3'])
	# 	for i in range(0,len(feature_set_1)):
	# 		writer.writerow([feature_set_1[i][0],fmt_feature_set(feature_set_1[i][1]),fmt_feature_set(feature_set_2[i][1]),fmt_feature_set(feature_set_3[i][1])])
