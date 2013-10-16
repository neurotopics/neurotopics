import neurosynth.analysis.reduce as nr
import nibabel
import pickle
import numpy as np
import json
from os import path

class atlas_labeler():
	"""	available atlases: brodmann, aal, combined
		example usage (get peaks for all brodmann areas)
		al = atlas_labeler()
		#load numpy array of data 
		data = al.load_atlas_roi_data('brodmann')
		#get labels as list
		labels = al.get_atlas_labels('brodmann')
	"""

	def __init__(self):
		"""initialize atlas_labeler object
			fields include dataset, doi_labels and atlas_list
		"""
		pickle_file_name = 'data/pickleddata.pkl'
		self.dataset = pickle.load(open(pickle_file_name, 'r'))

		#set up atlas files and atlas labels. atlas labels must be new-line limited, with names matching 
		#the numerical ordering of voxels in the map
		self.atlas_list = ['allvoxel/rbrodmann.nii','allvoxel/atlas_labels_combined.img','allvoxel/ROI_MNI_V4.nii', 'allvoxel/r30.nii']
		self.labels_list = ['allvoxel/rbrodmann.txt','allvoxel/names_atlas_labels_combined.txt','allvoxel/ROI_MNI_V4_names.txt']
		self.json_files = ['data/rbrodmann.json','data/atlas_labels_combined.json','data/ROI_MNI_V4.json','data/craddock.json']

		#this has dois in the same order
		self.doi_labels = self.dataset.image_table.ids
		self.ba_labels = self.get_atlas_labels('brodmann')
		self.aal_labels = self.get_atlas_labels('aal')
		self.comb_labels = self.get_atlas_labels('combined')

		#dois returned by dataset.imagetable.ids

		#get info for one region 
		#doi_label = doi_labels[1]
		#result_freq = res[1,:] #this gets peaks across studies for one region
		#region_name = al.ba_labels[1]
		#study_rois = res[:,1] #this gets the values for each ROI in atlas for one study
		#doi_label = self.doi_labels[1]


	#open each atlas and save results from neurosynth in json array (named by the name of the atlas)
	def save_roi_data(self,atlas='all'):
		"""save roi data for all atlases in atlas_list in a json file in data subfolder"""
		if atlas == 'all':
			for atlas in self.atlas_list:
				res = nr.average_within_regions(self.dataset,atlas)
				j=json.dumps(res.tolist())
				atlas_name = 'data/'+ path.basename(atlas)[:-4] + '.json'
				#self.json_files.append(atlas_name)
				jfile = open(atlas_name,'w')
				jfile.write(j)
				jfile.close()
		if atlas == 'craddock':
				atlas = self.atlas_list[3]
				res = nr.average_within_regions(self.dataset,atlas)
				j=json.dumps(res.tolist())
				atlas_name = 'data/'+ path.basename(atlas)[:-4] + '.json'
				jfile = open(atlas_name,'w')
				jfile.write(j)
				jfile.close()

	def load_atlas_roi_data(self,atlas_name):
		"""load saved json data from rois in atlas, atlas_name = brodmann, aal or combined, returns data as numpy array"""
		print ('Loading data from ' + self.return_atlas_file(atlas_name))
		if atlas_name == 'brodmann':
			json_file = self.json_files[0]
		elif atlas_name == 'combined':
			json_file = self.json_files[1]
		elif atlas_name == 'aal':
			json_file = self.json_files[2]
		elif atlas_name == 'craddock':
			json_file = self.json_files[3]
		json_data = open(json_file)
		data = json.load(json_data)
		nparray = np.array(data)
		return nparray

	def return_atlas_file(self,atlas_name):
		"""return atlas filename: brodmann, commbined or aal"""
		if atlas_name == 'brodmann':
			atlas_file = self.atlas_list[0]
		elif atlas_name == 'combined':
			atlas_file = self.atlas_list[1]
		elif atlas_name == 'aal':
			atlas_file = self.atlas_list[2]
		elif atlas_name == 'craddock':
			atlas_file = self.atlas_list[3]
		return path.basename(atlas_file)

	def get_atlas_labels(self,atlas_name):
		"""return the labels for each brain area in atlas. options = brodmann, combined, aal"""
		if atlas_name == 'brodmann':
			atlas_labels= self.labels_list[0]
		elif atlas_name == 'combined':
			atlas_labels= self.labels_list[1]
		elif atlas_name == 'aal':
			atlas_labels = self.labels_list[2]
		f = open(atlas_labels,'r')
		names = f.readlines()
		names = [x.strip('\n') for x in names]
		return names

	#just used to save list of brodmann areas (each brodmann area has a voxel value corresponding to the brodmann area)
	def generate_brodmann_labels(self):
		regions = self.dataset.volume.mask('allvoxel/rbrodmann.nii')
		bareas = np.unique(regions)
		ba_list = [];
		for ba in bareas:
			ba_list.append('BA ' + str(ba))
		ba_file = open('allvoxel/rbrodmann.txt','w')
		for line in ba_list:
			ba_file.write(line+'\n')
		ba_file.close()


