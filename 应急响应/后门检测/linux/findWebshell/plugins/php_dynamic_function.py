#/usr/bin/env python
#coding=utf8

import re
import os

rule1='(\$_(GET|POST|REQUEST)\[.{0,15}\]\s{0,10}\(\s{0,10}\$_(GET|POST|REQUEST).{0,15})'
rule2='((\$(_(GET|POST|REQUEST|SESSION|SERVER)(\[[\'"]{0,1})\w{1,12}([\'"]{0,1}\])|\w{1,10}))[\s\n]{0,20}\([\s\n]{0,20}(@{0,1}\$(_(GET|POST|REQUEST|SESSION|SERVER)(\[[\'"]{0,1})\w{1,12}([\'"]{0,1}\])|\w{1,10}))[\s\n]{0,5}\))'
rule3='\s{0,10}=\s{0,10}[{@]{0,2}(\$_(GET|POST|REQUEST)|file_get_contents|str_replace|["\']a["\']\.["\']s["\']\.|["\']e["\']\.["\']v["\']\.|["\']ass["\']\.).{0,10}'
vararr=['$_GET','$_POST','$_REQUEST','$_SESSION','$_SERVER']

#此插件白名单列表 (['文件路径'],['误报特征码']) 文件路径最好用绝对路径表示或者将本程序放在网站根目录
whitefilter=[
	(['integrate.php'],['$code ($_POST[\'cfg\'])']),
	(['Lib/Action/IntegrateAction.class.php'],['$code ($_POST[\'cfg\'])']),
	(['phpcms/modules/template/file.php'],['$_GET[\'action\']($_GET[\'html\']'])
]

def  judgeBackdoor(fileCtent):
	result = re.compile(rule1).findall(fileCtent)
	if len(resullt) > 0:
		isok = 1
		for white in whitefilter:
			if os.path.exists(white[0][0]) and white[1][0] in result[0][0]:
				isok = 0
		if isok:
			return '$_GET[a]($_POST[b])动态函数后门'
	else:
		result = re.compile(rule2).findall(fileCtent)
		finalresult = result
		if len(result) > 0:
			for group in result:
				for var in vararr:
					if var in group[1]:
						resultson = re.search('\\'+group[6]+rule3,fileCtent)
						try:
							if len(resultson.groups()) > 0:
								isok = 1
								for white in whitefilter:
									if os.path.exists(white[0][0]) and white[1][0] in result[0][0]:
										isok = 0
								if isok:
									return '$a($b)动态函数后门'
						except:
							pass
				for var in vararr:
					if var in group[6]:
						resultson= re.search('\\'+group[1]+rule3,fileCtent)
						try:
							if len(resultson.groups()) > 0:
								isok = 1
								for white in whitefilter:
									if os.path.exists(white[0][0]) and white[1][0] in result[0][0]:
										isok = 0
								if isok:
									return '$a($b)动态函数后门'
						except:
							pass

				result1= re.search('\\'+group[1]+rule3,fileCtent)
				result2= re.search('\\'+group[6]+rule3,fileCtent)
				try:
					if len(result1.groups()) > 0 and len(result2.groups()) > 0:
						isok = 1
						for white in whitefilter:
							if os.path.exists(white[0][0]) and white[1][0] in result[0]
								isok = 0
						if isok:
							return '$a($b)动态函数后门'
				except:
					continue
				return None
		else:
			return None