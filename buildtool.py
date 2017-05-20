import logging
import re

class Builder:
	metatags = []

	def __init__(self):
		self.data = []
		# TODO: generate global metatag regexes from configuration
		self.metatags.append(re.compile(r'{{-content-}}', re.IGNORECASE))

	def generatePage(self, source, template, destination):
		logging.info("Building: source %s with template %s: %s", source, template, destination)
		s = open(source, 'r')
		t = open(template, 'r')
		d = open(destination, 'w')
		# TODO: read source and parse metadata
		tags = self.metatags
		# TODO: convert source MD to HTML
		content = s.read()
		# Process template file, make replacements
		for line in t:
			for tag in tags:
				if tag.search(line):
					line = tag.sub(content, line)
			d.write(line)
		s.close()
		t.close()
		d.close()

if __name__ == "__main__":
	print "\nERROR: This file does not execute on its own, use 'mdwebsite'\n"
