from common import *

def preprocess(filename):
	def preprocessText(text):
		def removeHTML(text):
			return text
		def removeURL(text):
			return text
		def removeAt(text):
			return text
		def removeHashTag(text):
			return text

		text = removeHTML(text)
		text = removeURL(text)
		text = removeAt(text)
		text = removeHashTag(text)
		return text

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