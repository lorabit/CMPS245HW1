from common import *
from feature_generation import *
from lsi import *
from preprocess import *
from clustering import *

def process(dataset, k = 5, n_topic = 100):
	print '###### Processing '+dataset+" ..."
	preprocess(dataset)

	print '##### Generating feature set 1 ...'
	feature_set_1 = unigram_feature(dataset)
	feature_set_1_sparse = words2sparse(feature_set_1)

	print '##### Generating feature set 2 ...'
	feature_set_2 = unigram_tfidf(dataset)
	feature_set_2_sparse = words2sparse(feature_set_1)

	print '##### Generating feature set 3 ...'
	feature_set_3 = unigram_tfidf_normalization(dataset)
	feature_set_3_sparse = words2sparse(feature_set_1)

	print '##### Generating feature set 4 using LSI ...'
	feature_set_4_matrix = lsi(feature_set_3, n_topic)

	print '##### Clustering with feature set 1'
	labels_fs1 = clustering(feature_set_1_sparse,k)

	print '##### Clustering with feature set 2'
	labels_fs2 = clustering(feature_set_2_sparse,k)

	print '##### Clustering with feature set 3'
	labels_fs3 = clustering(feature_set_3_sparse,k)

	print '##### Clustering with feature set 4'
	labels_fs4 = clustering(feature_set_4_matrix,k)

	print '##### Generating result csv file ...'
	original_data = []
	with open(dataset,'rb') as infile:
		rows = csv_reader(infile)
		line = 0
		for row in rows:
			line += 1
			if line == 1:
				continue
			original_data += [[row[0],row[10]]]
	with open(result_filename(dataset),'wb') as outfile:
		writer = csv_writer(outfile)
		writer.writerow(['tweet id','text','label 1','label 2','label 3','label 4','feature set 1','feature set 2','feature set 3','feature set 4'])
		for index in range(0,len(original_data)):
			row = [original_data[index][0],original_data[index][1]]
			row += [labels_fs1[index],labels_fs2[index],labels_fs3[index],labels_fs4[index]]
			row += [fmt_feature_set(feature_set_1[index][1]),fmt_feature_set(feature_set_2[index][1]),fmt_feature_set(feature_set_3[index][1]),','.join([str(v) for v in feature_set_4_matrix[index]])]
			writer.writerow(row)

if __name__ == '__main__':
	process(dataset_clinton,10)