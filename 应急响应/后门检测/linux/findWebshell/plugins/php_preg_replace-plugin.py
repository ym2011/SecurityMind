#/usr/bin/env python
#coding=utf8

import re

keyword = "preg_replace"
rule = '(preg_replace[\s\n]{0,10}\([\s\n]{0,10}((["\'].{0,15}[/@\'][is]{0,2}e[is]{0,2}["\'])|\$[a-zA-Z_][\w"\'\[\]]{0,15})\s{0,5},\s{0,5}.{0,40}(\$_(GET|POST|REQUEST|SESSION|SERVER)|str_rot13|urldecode).{0,30})'
backdoorType = "preg_replace后门"

#判断是否存在后门函数
def  judgeBackdoor(fileCtent):
	if keyword in fileCtent:
		result = re.compile(rule).findall(fileCtent)
		if len(result) > 0:
			return  backdoorType
	else:
		return None