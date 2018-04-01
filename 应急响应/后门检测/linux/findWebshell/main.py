#!/usr/bin/env python
#coding=utf8

import glob, os
from optparse import OptionParser
from filterShell import FilterShell
from getFileTime import getFileTime
from scanShell import *
from createHtml import createHtml

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("-p", "--path", dest="path",
		help="input web directory filepath", metavar="PATH")
	parser.add_option("-o", "--output", dest="output",
		help="create a html report")
	parser.add_option("-e", "--ext", dest="ext",
		help="define what's file format to scan", metavar="php|asp|aspx|jsp|all")

	(options, args) = parser.parse_args()

	#黑名单列表
	blackList = []
	#名字字典
	fileList = {}
	#结果列表
	resList =  []

	#检测是否输入合法的路径和要扫描的类型
	if options.ext == None or options.path == None:
		parser.error("输入的参数不正确!")

	#获取文件绝对路径
	for root, dirs, files in os.walk(options.path):
		for filename in files:
			fullpath = os.path.join(root, filename)
			fileList[filename] = fullpath

	#过滤类
	FilterShell = FilterShell()

	#文件名过滤
	for filename in fileList.keys():
		res = FilterShell.filename(options.ext, filename)
		if res:
			#获取后门类型，文件修改时间，文件路径
			fullpath = fileList.get(filename)
			mtime = getFileTime(fullpath)
			filemode = "一般类型"
			resList.append([fullpath, filemode, mtime])
			blackList.append(fullpath)
		else:
			pass

	#根据后门特征码过滤
	for filename in fileList.keys():
		fullpath = fileList.get(filename)
		if fullpath not in blackList:
			with open(fullpath, "rb") as fp:
				ctent = fp.read()
				filemode = FilterShell.content(options.ext, ctent)
				#获取后门类型，文件修改时间，文件路径
				if filemode:
					mtime = getFileTime(fullpath)
					resList.append([fullpath, filemode, mtime])
					blackList.append(fullpath)
				else:
					pass
		else:
			pass

      #正则匹配后门语法
	scan(options.path, options.ext, blackList, resList)

	#处理后门列表
	l = len(resList)
	for i in xrange(l):
		resList[i][0] = os.path.abspath(resList[i][0])

	#生成报告
	if options.output:
		fp = open(options.output + '.html', 'w')
	else:
		fp = open('report.html', 'w')
	html = createHtml(resList)
	fp.write(html)