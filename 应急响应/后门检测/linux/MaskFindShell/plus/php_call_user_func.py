#!/usr/bin/python2.7
#coding:utf-8

import re

rule='(call_user_func[\s\n]{0,25}\(.{0,25}\$_(GET|POST|REQUEST).{0,15})'

def Check(filestr,filepath):
    if 'call_user_func' in filestr:
        result = re.compile(rule).findall(filestr)
        if len(result)>0:
            return result,'call_user_func'
    else:
        return None
