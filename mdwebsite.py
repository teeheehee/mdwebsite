#!/usr/bin/env python

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

def printHelp():
	print """\

Usage: mdwebsite [OPTIONS]

    -h        Display this usage message
    build     Build the static website to a local output directory
    deploy    Archive existing deployed website, deploy latest build
"""
	sys.exit()

if __name__ == "__main__":

	if len(sys.argv) != 2:
		printHelp()

	if sys.argv[1] == "build":
		print "Building!\n"
		bt = buildtool.Builder()
		bt.generatePage("./content/index.html", "./templates/FrontPage.html", "./build/index.html")
	elif sys.argv[1] == "deploy":
		print "Deploy!\n"
	else:
		printHelp()
