# L. Amber Wilcox-O'Hearn 2013
# Neurotopics/scripts/extract_counts.py

import pickle

feature_file_name = 'data/features.txt'
database_file_name= 'data/database.txt'
pickle_file_name = 'data/pickleddata.pkl'

features = [x.split() for x in open(feature_file_name, 'r').readlines()]
database = [x.split() for x in open(database_file_name, 'r').readlines()[0].split('\r')]
dataset = pickle.load(open(pickle_file_name, 'r'))




