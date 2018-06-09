#!coding=utf-8

'''
jsp木马判断

'''

import re

keyword_a=r"string pwd.?=.?[^;]*;"   ##jsp木马文件内容存在密码pwd字段
keyword_b=r"string ([^=]*)=[^;]*;"     ##jsp参数追踪
keyword_d=r'"[^"]*"\.equals\(request\.getparameter\(.*\)\)'  ##另类木马


def Check(filestr,filepath):

	filestr=filestr.lower()
	tag=0

	a=re.search(keyword_a,filestr)

	b=re.compile(keyword_b)
	f=b.findall(filestr)

	d=re.search(keyword_d,filestr)
	
	if a:
		tag=1
		result=((a.group(),),)

	if b:
		for i in f:
			try:
				keyword_c=r"request\.getparameter"+"("+i.lower()+")"
				c=re.search(keyword_c,filestr)
				if c:
					tag=1
					result=((c.group(),),)
					break
			except:
				pass

	if d:
		tag=1
		result=((d.group(),),)

	if tag==1:
		return result,'Danger'

	return None


