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

	with open(filename, 'rb') as csvfile:
		rows = csv.reader(csvfile, delimiter=',', quotechar='"')
		line = 0
		for row in rows:
			line += 1
			if line == 1:
				continue
			print preprocessText(row[10])
			break


if __name__ == '__main__':
	preprocess('data/clinton-50k.csv')