import os
import configtool

class Files:
	contentPath = ""
	data = []
	copyFiles = []
	translateFiles = []

	def __init__(self, config):
		content_path = os.path.abspath(config.get('content_path'))
		print(content_path)
		self.find_files(content_path)

	def find_files(self, root_dir): 
		for contents in os.listdir(root_dir): 
			path = os.path.join(root_dir, contents) 
			#print path
			#data.append(path)
			if os.path.isdir(path): 
				self.find_files(path)
			else:
				self.data.append(path)

	def get_all(self):
		return self.data

if __name__ == "__main__":
	print("\nERROR: This file does not execute on its own, use 'mdwebsite'\n")
	print("While we're here, let's read config.json and see what files we have:\n")
	config = configtool.Config("config.json")
	f = Files(config)
	print(f.get_all())