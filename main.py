#!/usr/bin/python

import sys

def is_one_to_one_mapping(s1, s2):
	l1 = len(s1)
	l2 = len(s2)

	if l1 > 256:
		return False

	if l1 <= l2:

		char_set = [False] * 128

		for i in range(l1):

			val = ord(s1[i])
			
			if char_set[val]:
				return False

			char_set[val]=True

		return True
	return False

s1 = sys.argv[1]
s2 = sys.argv[2]

if is_one_to_one_mapping(s1, s2):
	print("true")
else:
	print("false")
	
