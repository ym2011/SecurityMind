#!/usr/bin/python2.7
#coding:utf-8

import re

rule1='(preg_replace[\s\n]{0,10}\([\s\n]{0,10}((["\'].{0,15}[/@\'][is]{0,2}e[is]{0,2}["\'])|\$[a-zA-Z_][\w"\'\[\]]{0,15})\s{0,5},\s{0,5}.{0,40}(\$_(GET|POST|REQUEST|SESSION|SERVER)|str_rot13|urldecode).{0,30})'

def Check(filestr,filepath):

    if 'preg_replace' in filestr:
        result = re.compile(rule1).findall(filestr)
        if len(result)>0:
            return result,'preg_replace'
    else:
        return None
