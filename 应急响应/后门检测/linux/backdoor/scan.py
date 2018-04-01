#!/usr/bin/python
# -*- coding: utf-8 -*-

#Version:       0.02
#Create:        2016-06-13
#Authoruis:     ym2011

import sys
import getopt
import core 

def Usage():
	print 'scan usage:'
	print '使用：scan.py filepath'
	print '-h,--help: 获取帮助信息.'
	print '-v, --version: 获取scan版本'
	print '-p,--path: 指定将要扫描的路径'
	print '-l,--low: 系统/数据库弱密码扫描'
def Version():
	print 'scan 0.02 BASE'
def OutPut(args):
	print 'Hello, %s'%args
def main(argv):
	try:
		opts, args = getopt.getopt(argv[1:], 'hvp:', ['path='])
	except getopt.GetoptError, err:
		print str(err)
		Usage()
		sys.exit(2)
	if len(opts) == 0:
		if len(args):
			core.start(args[0])
		else:
			print "scanning [options] [param]"
	for o, a in opts:
		if o in ('-h', '--help'):
			Usage()
			sys.exit(1)
		elif o in ('-v', '--version'):
			Version()
			sys.exit(0)
		elif o in ('-p',):
                        core.start(a)
			sys.exit(0)
		else:
			Usage()
			sys.exit(3)

if __name__ == '__main__':
	main(sys.argv)
