#/usr/bin/env python
#coding=utf8

import re

rule=r'(array_map[\s\n]{0,20}\(.{1,5}(eval|assert|ass\\x65rt).{1,20}\$_(GET|POST|REQUEST).{0,15})'

def  judgeBackdoor(fileCtent):
	if 'array_map' in fileCtent:
		result = re.compile(rule).findall(fileCtent)
		if len(result) > 0:
			return 'array_map后门'
		else:
			return None