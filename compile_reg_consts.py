import re

PATTERN1 = re.compile(r" {2,}|\n")
PATTERN2 = re.compile(r"<vim-select-item-title.+</vim-select-item-title>")
PATTERN3 = re.compile(r"#+")
PATTERN4 = re.compile(r"translateY\((\w*?)px\)")
PATTERN5 = re.compile(r"\((.*?)\)")
PATTERN6 = re.compile(r"(_{4,})+?")
PATTERN7 = re.compile(r"\t|\n| {2,}")
PATTERN8 = re.compile(r"\(.*?\)")
