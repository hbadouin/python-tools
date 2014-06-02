#!/usr/bin/python
""" Header.

Description of what the script is doing.

"""

import os
import sys
import argparse

# Some of my favorite modules. Just remove the leading # to import them.

#import numpy as np
#from matplotlib import pyplot as plt
#import csv
#import itertools
#import subprocess
#import re

#======== main function

def main() :
	""" Header.

	"""
	args = parse_args() 
	infile		= args.infile
	
	try :
		f = open(infile, "r")
	except :
		print "Unable to open input file"
		sys.exit(1)

	f.close()

# parse arguments

def parse_args() :
	parser = argparse.ArgumentParser()
	parser.add_argument("--infile","-f", required = True, help = "input file")
	args = parser.parse_args()
	return args


#=========== to have the main function executed when and only when the script is executed

if __name__ == '__main__':
	main()
