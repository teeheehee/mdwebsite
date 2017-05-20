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

import logging

def printHelp():
	print """\
Usage: mdwebsite [OPTIONS]
    -h        Display this usage message
    build     Build the static website to a local output directory
    deploy    Archive existing deployed website, deploy latest build
"""

if __name__ == "__main__":
    printHelp()
