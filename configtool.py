import json

class Config:
	data = []

	def __init__(self, configfile):
		c = open(configfile)
		self.data = json.load(c)
		c.close()

	def get(self, key):
		return self.data[key]

	def get_all(self):
		return self.data

if __name__ == "__main__":
	print("\nERROR: This file does not execute on its own, use 'mdwebsite'\n")
	print("While we're here, let's read config.json and see how it parses:\n")
	c = Config("config.json")
	print(c.get_all())
