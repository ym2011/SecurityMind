#/usr/bin/env python
#coding=utf8

import re

rule1='([^\'"](include|require)(_once){0,1}\s{0,5}(\s{0,5}|\(\s{0,5})["\']([\.\w\,/\\\+-_]{1,60})["\']\s*\){0,1})'
rule2='((include|require)(_once){0,1}(\s{0,5}|\s{0,5}\(\s{0,5})[\'"]{0,1}(\$(_(GET|POST|REQUEST|SERVER)(\[[\'"]{0,1})\w{0,8}([\'"]{0,1}\])|[\w]{1,15}))[\'"]{0,1})'
rule3='\s{0,10}=\s{0,10}([{@]{0,2}\$_(GET|POST|REQUEST)|[\'"]{0,1}php://input[\'"]{0,1}|file_get_contents).{0,20}'
vararr=['$_GET','$_POST','$_REQUEST','$_SERVER']
Whiterule = ['.php','$','templates','.html']

def  judgeBackdoor(fileCtent):
	if 'include' in fileCtent or 'require' in fileCtent:
		result = re.compile(rule1).findall(fileCtent)
		if len(result) > 0:
			resultlist = []
			for key in result:
				isok = 1
				for Whitestr in Whiterule:
					if Whitestr in key[4].lower():
						isok = 0
				if isok == 1:
					resultlist.append(key)
			if len(resultlist) > 0:
				return 'include|require(_once)非法引用后门'

		result = re.compile(rule2).findall(fileCtent)
		if len(result) > 0:
			varlist = ''
			for group in result:
				if group[4] in varlist:
					continue
				else:
					varlist += group[4] + '--'
				for var in vararr:
					if var in group[4]:
						return 'include|require(_once)非法引用动态参数后门'
				resultson = re.search('\\'+group[4]+rule3,fileCtent)
				try:
					if len(resultson.groups()) > 0:
						return 'include|require(_once)非法引用动态参数后门'
				except:
					continue
		return None
	else:
		return None
