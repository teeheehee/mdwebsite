import logging
import markdown
import re

class Builder:
	metatags = []

	def __init__(self):
		self.data = []
		# TODO: generate global metatag regexes from configuration
		self.metatags.append(re.compile(r'{{-content-}}', re.IGNORECASE))
		self.md = markdown.Markdown(
			output_format = "html5",
			extensions = ['markdown.extensions.meta',
				'markdown.extensions.codehilite',
				'markdown.extensions.toc',
				'markdown.extensions.wikilinks',
				'markdown.extensions.extra',
				'markdown.extensions.nl2br'])

	def generate_page(self, source, template, destination):
		logging.info("Building: source %s with template %s: %s",
			source, template, destination)
		# Open all related files
		s = open(source, 'r')
		t = open(template, 'r')
		d = open(destination, 'w', encoding="utf-8", errors="xmlcharrefreplace")
		# Process MD file
		content = s.read()
		htmlcontent = self.md.reset().convert(content)
		# print(self.md.Meta)
		# Prepare search and replace tags
		# TODO: how to handle replacement choices for configurable metatags, or are they all special cases?
		tags = self.convert_metadata_to_tags(self.md.Meta)
		for tag in self.metatags:
			newtag = tag, htmlcontent
			tags.append(newtag)
		# Process template file and write destination content
		for line in t:
			for tag in tags:
				search = tag[0]
				replacement = tag[1]
				if search.search(line):
					line = search.sub(replacement, line)
			d.write(line)
		# Cleanup
		s.close()
		t.close()
		d.close()

	def convert_metadata_to_tags(self, metadata):
		tags = []
		for key, replacement in metadata.items():
			search = re.compile("{{{{-{0}-}}}}".format(key), re.IGNORECASE)
			tag = search, ", ".join(replacement)
			tags.append(tag)
		return tags

if __name__ == "__main__":
	print("\nERROR: This file does not execute on its own, use 'mdwebsite'\n")
