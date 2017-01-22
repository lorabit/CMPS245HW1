import csv

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

	with open(filename[:-4]+'_preprocessed.csv','wb') as outfile:
		writer = csv.writer(outfile, delimiter=',', quotechar='"')
		with open(filename, 'rb') as csvfile:
			rows = csv.reader(csvfile, delimiter=',', quotechar='"')
			line = 0
			for row in rows:
				line += 1
				if line == 1:
					continue
				writer.writerow([row[0], preprocessText(row[10])])


if __name__ == '__main__':
	preprocess('data/clinton-50k.csv')