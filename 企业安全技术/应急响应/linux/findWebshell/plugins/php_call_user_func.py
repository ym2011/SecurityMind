#/usr/bin/env python
#coding=utf8

import re

rule='(call_user_func[\s\n]{0,25}\(.{0,25}\$_(GET|POST|REQUEST).{0,15})'

def  judgeBackdoor(fileCtent):
	if 'call_user_func' in fileCtent:
		result = re.compile(rule).findall(fileCtent)
		if len(result) > 0:
			return 'call_user_func后门'
		return None
	else:
		return None