#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:	0.02
#Create:	2016-06-13
#Authoruis:	ym2011

import os


list = []
#遍历目录
def traversal_dir(filepath, prin=False):
	#遍历filepath下所有文件，包括子目录
	files = []
	try:
		files = os.listdir(filepath)
	except OSError:
		pass
		print filepath,"\t The folder does not exist!"
	if len(files):
		for fi in files:
			fi_d = os.path.join(filepath,fi)            
			if os.path.isdir(fi_d):
				traversal_dir(fi_d, prin)        
			else:
				if prin :
					print os.path.join(filepath,fi_d)
				list.append(os.path.join(filepath,fi_d))#添加遍历到的文件
	return list

def print_files(self):
	for ls in list:
		print ls


def test():
	#递归遍历所有文件
	traversal_dir('Desktop')
	print_files()


if __name__ == '__main__':
	test()
