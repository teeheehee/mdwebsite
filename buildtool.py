import logging
import markdown
import re

class Builder:
	metatags = []
	config = []

	def __init__(self, config):
		# Generate global metatag regexes from configuration
		self.metatags = self.convert_metadata_to_tags(config.get('replacements'))
		# Special case: replace all content with generated data
		pattern = "content"
		search = re.compile("{{{{-{0}-}}}}".format(pattern), re.IGNORECASE)
		replacement = ""
		tag = pattern, search, replacement
		self.metatags.append(tag)
		# Prepare markdown renderer
		self.md = markdown.Markdown(
			output_format = "html5",
			extensions = ['markdown.extensions.meta',
				'markdown.extensions.codehilite',
				'markdown.extensions.toc',
				'markdown.extensions.wikilinks',
				'markdown.extensions.extra',
				'markdown.extensions.nl2br'])

	def generate_page(self, source, template, destination):
		logging.info("Building: source {0} with template {1}: {2}".format(
			source, template, destination))
		# Open all related files
		s = open(source, 'r')
		t = open(template, 'r')
		d = open(destination, 'w', encoding="utf-8", errors="xmlcharrefreplace")
		# Process MD file
		content = s.read()
		htmlcontent = self.md.reset().convert(content)
		# Prepare search and replace tags
		# TODO: how to handle replacement choices for configurable metatags, or are they all special cases?
		tags = self.prepare_all_tags(self.md.Meta, htmlcontent)
		# Process template file and write destination content
		for line in t:
			for tag in tags:
				pattern = tag[0]
				search = tag[1]
				replacement = tag[2]
				if search.search(line):
					logging.info("Pattern {0} found and replaced".format(pattern))
					line = search.sub(replacement, line)
			d.write(line)
		# Cleanup
		s.close()
		t.close()
		d.close()

	def prepare_all_tags(self, metadata, htmlcontent):
		# Merge well-known tags from config with overrides from markdown metadata
		# TODO: well-known tags in configuration, other sources of replacement
		alltags = self.convert_metadata_to_tags(metadata)
		for tag in self.metatags:
			pattern = tag[0]
			search = tag[1]
			replacement = tag[2]
			if pattern in metadata:
				continue
			# TODO: other special cases
			if pattern == "content":
				newtag = pattern, search, htmlcontent
				alltags.append(newtag)
			else:
				alltags.append(tag)
		return alltags

	def convert_metadata_to_tags(self, metadata):
		tags = []
		for key, replacement in metadata.items():
			search = re.compile("{{{{-{0}-}}}}".format(key), re.IGNORECASE)
			newreplacement = ""
			if isinstance(replacement, str):
				newreplacement = replacement
			else:
				newreplacement = ", ".join(replacement)
			tag = key, search, newreplacement
			tags.append(tag)
		return tags

if __name__ == "__main__":
	print("\nERROR: This file does not execute on its own, use 'mdwebsite'\n")
