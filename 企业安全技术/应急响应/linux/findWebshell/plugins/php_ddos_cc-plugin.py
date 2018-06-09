#/usr/bin/env python
#coding=utf8

import re
import os

keywords = [
	'启动自动攻击',
	'xxddos',
	'phpddos',
	'fsockopen("udp:',
	'fsockopen("tcp:',
	'$_get["moshi"]=="udp"'
]

#此插件白名单列表 (['文件路径'],['误报特征码'])
whitefilter = [
	(['install/svinfo.php'], ['fsockopen("tcp:']),
]

def  judgeBackdoor(fileCtent):
	fileCtent = fileCtent.lower()
	#纯关键词查找-暂不确定后门
	for key in keywords:
		if key in fileCtent:
			isok = 1
			for white in whitefilter:
				if os.path.exists(white[0][0]) and white[1][0] in key:
					isok = 0
			if isok:
				return 'PHP ddos_cc攻击脚本'
	return None