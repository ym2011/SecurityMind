#!/usr/bin/env python
#coding=utf8

import os
import time

def getFileTime(filepath):
	fileModifyTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filepath)))
	return fileModifyTime
