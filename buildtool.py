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
		s = open(source, 'r')
		t = open(template, 'r')
		d = open(destination, 'w', encoding="utf-8", errors="xmlcharrefreplace")
		# TODO: read source and parse metadata
		tags = self.metatags
		# TODO: convert source MD to HTML
		content = s.read()
		htmlcontent = self.md.reset().convert(content)
		# print(self.md.Meta)
		# print(html)
		# Process template file, make replacements
		for line in t:
			for tag in tags:
				if tag.search(line):
					line = tag.sub(htmlcontent, line)
			d.write(line)
		s.close()
		t.close()
		d.close()

if __name__ == "__main__":
	print("\nERROR: This file does not execute on its own, use 'mdwebsite'\n")
