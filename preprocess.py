from common import *
from nltk.tokenize import TweetTokenizer
import re

def preprocess(filename):
	tknzr = TweetTokenizer()

	def preprocessText(text):
		new_tokens = []
		def removeHTML(tokens):
			return tokens

		def removeURL(tokens):
			new_tokens = []
			for token in tokens:
				if token[0:4] == 'http' or token[0:3] == 'www':
					continue

				else:
					new_tokens.append(token)

			return new_tokens

		def removeAt(tokens):
			new_tokens = []
			for token in tokens:
				if token[0] == '@':
					token = token[1:]
					new_tokens.append(token)
				else:
					new_tokens.append(token)
			return new_tokens



		def removeHashTag(tokens):
			cnt = 0
			for token in reversed(tokens):
				if len(token) != 0 and token[0] == '#':
					tokens.remove(token)
				else:
					break


			return tokens

		def removeNULL_Single(tokens):

			for token in tokens:
				if len(token) == 0:
					print tokens
					tokens.remove(token)
				else:
					continue
			
			for token_1 in tokens:
				if len(token_1) == 1:
					tokens.remove(token_1)
				else:
					continue
			
			return tokens

		def test_wrong(tokens):
			for token in tokens:
				if len(token) == 1 or len(token) == 0:
					return 1
			return 0

		def print_wrong(tokens):
			for token in tokens:
				if len(token) == 1 or len(token) == 0:
					print token
					print tokens

		# print text
		tokens = tknzr.tokenize(text)
		#print tokens
		tokens = removeHTML(tokens)
		while (test_wrong(tokens) == 1):
			tokens = removeNULL_Single(tokens)
			
		tokens = removeURL(tokens)
		tokens = removeAt(tokens)
		tokens = removeHashTag(tokens)
		


		# print tokens
		# print tokens
		return ' '.join(tokens)

	with open(preprocessed_filename(filename),'wb') as outfile:
		writer = csv_writer(outfile)
		with open(filename, 'rb') as csvfile:
			rows = csv_reader(csvfile)
			line = 0
			for row in rows:
				line += 1
				if line == 1:
					continue
				writer.writerow([row[0], preprocessText(row[10])])


if __name__ == '__main__':
	preprocess(dataset_clinton)