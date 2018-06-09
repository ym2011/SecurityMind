#!/usr/bin/python2.7
#coding:utf-8

import re

rule=r'(array_map[\s\n]{0,20}\(.{1,5}(eval|assert|ass\\x65rt).{1,20}\$_(GET|POST|REQUEST).{0,15})'

def Check(filestr,filepath):
    if 'array_map' in filestr:
        result = re.compile(rule).findall(filestr)
        if len(result)>0:
            return result,'array_map'
    else:
        return None
