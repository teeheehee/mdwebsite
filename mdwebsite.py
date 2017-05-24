#!/usr/bin/env python3

##
#	mdwebsite
#
#	Purpose:
#		Tool for building and deploying a static website with support for Markdown files.
#
#	Author:
#		Dan Kissam, teeheehee@gmail.com
#
#	Version:
#		Refer to VERSION.md

import sys
import logging
import buildtool
import configtool

def printHelp():
	print("""\

Usage: mdwebsite [OPTIONS]

    -h        Display this usage message
    build     Build the static website to a local output directory
    deploy    Archive existing deployed website, deploy latest build
""")
	sys.exit()

if __name__ == "__main__":

	if len(sys.argv) != 2:
		printHelp()

	logging.basicConfig(level=logging.INFO)
	config = configtool.Config("config.json")

	if sys.argv[1] == "build":
		logging.info("Performing website build")
		bt = buildtool.Builder(config)
		contentFile = config.get('content_path') + "index.md"
		templateFile = config.get('templates_path') + "FrontPage.html"
		outputFile = config.get('output_path') + "index.html"
		bt.generate_page(contentFile, templateFile, outputFile)
	elif sys.argv[1] == "deploy":
		logging.error("Deploy option is not yet implemented")
	else:
		printHelp()
