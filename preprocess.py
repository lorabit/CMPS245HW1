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
				if token.lower()[0:4] == 'http' or token.lower()[0:3] == 'www' or token[0:2] == ':/':
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
			new_tokens = []
			for token in reversed(tokens):
				if len(token) != 0 and token[0] == '#':
					#tokens.remove(token)
					cnt = cnt +1
				else:
					break
			new_tokens = tokens[0:len(tokens)-cnt]
			#print cnt



			return new_tokens

		def removeNULL_Single(tokens):

			new_tokens = []
			for token in tokens:
				if len(token) == 0 or len(token) == 1 or token[0:3] == '...':
					continue
				else:
					new_tokens.append(token)
			
			
			return new_tokens

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
		# print tokens
		tokens = removeHTML(tokens)
		# print tokens
		
		tokens = removeNULL_Single(tokens)
			
		tokens = removeURL(tokens)
		tokens = removeAt(tokens)
		#print tokens
		tokens = removeHashTag(tokens)
		


		# print tokens
		# print tokens
		return ' '.join(tokens)

	# print preprocessText('[ #Luiis_3x ] This Might Be The Dumbest Line Of Inquiry At The Benghazi Hearing: EmbedContent(56... https://t.co/Ieu6bqE6bY [ #Luiis_3x ]')

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