import csv

dataset_clinton = 'data/clinton-50k.csv'
dataset_trump = 'data/trump-50k.csv'

def csv_writer(outfile):
	return csv.writer(outfile, delimiter=',', quotechar='"')

def csv_reader(infile):
	return csv.reader(infile, delimiter=',', quotechar='"')

def preprocessed_filename(filename):
	return filename[:-4]+'_preprocessed.csv'