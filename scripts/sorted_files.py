dataset_file = 'data/database.txt'
dois = open('/Users/jmollick/Dropbox/NeuroTopics_Shared/data_metadata/neurosynth_sql_meta_DOI.txt','r').readlines()
docfile = open('/Users/jmollick/Dropbox/NeuroTopics_Shared/data_fulldocs/docwordfreqs.txt','r').readlines()

#making a list of all our dois
doi_copy = []
for i in dois:
	doi_copy.append(i.strip('\n'))

#opening up the dataset
database = [x.split() for x in open(dataset_file, 'r').readlines()[0].split('\r')]
database.pop(0)
doi_list = []

#add all the dois from the database to a list
for i in database:
	doi_list.append(i[4])

#grab only the unique ones
uniq_dois = list(set(doi_list))

