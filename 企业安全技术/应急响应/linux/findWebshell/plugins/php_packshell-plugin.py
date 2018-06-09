#/usr/bin/env python
#coding=utf8

import re

rule='gzdeflate|gzcompress|gzencode'

#此插件白名单列表 (['文件路径'],['误报特征码'])
whitefilter=[]

def  judgeBackdoor(fileCtent):
	result = re.search(rule, fileCtent)
	try:
		if result.group():
			if '打包' in fileCtent and 'unix2DosTime' in fileCtent:
				isok = 1
				for white in whitefilter:
					if white[0][0] in filepath.replace('\\', '/') and white[1][0] in key:
						isok = 0
				if isok:
					return 'PHP 文件打包后门程序'
	except:
		pass
	return None
