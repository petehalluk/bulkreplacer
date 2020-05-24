#!/usr/bin/python

import glob
import sys
import fileinput

def replace_in_file(filename, text_to_search, replacement_text):
	with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
		for line in file:
			print(line.replace(text_to_search, replacement_text), end='')
			
def replace_in_files(file_pattern, text_to_search, replacement_text):
	files = glob.glob(file_pattern)
	for file in files:
		replace_in_file(file, text_to_search, replacement_text)

if __name__ == "__main__":
	if len(sys.argv) < 4:
		print(f"Usage: bulkreplacer.py <text_to_search> <replacement_text> <file_pattern>")
		sys.exit(1)
	find = sys.argv[1]
	replace = sys.argv[2]
	file_pattern = sys.argv[3]
	replace_in_files(file_pattern, find, replace)
