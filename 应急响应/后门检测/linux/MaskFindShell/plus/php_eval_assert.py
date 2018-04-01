#!/usr/bin/python2.7
#coding:utf-8

import re

rule='((eval|assert)[\s|\n]{0,30}\([\s|\n]{0,30}(\\\\{0,1}\$((_(GET|POST|REQUEST|SESSION|SERVER)(\[[\'"]{0,1})[\w\(\)]{0,15}([\'"]{0,1}\]))|\w{1,10}))\s{0,5}\))'
rule1='((eval|assert)[\s|\n]{0,30}\((gzuncompress|gzinflate\(){0,1}[\s|\n]{0,30}base64_decode.{0,100})'
rule2='\s{0,10}=\s{0,10}([{@]{0,2}\\\\{0,1}\$_(GET|POST|REQUEST)|file_get_contents|["\']a["\']\.["\']s["\']\.|["\']e["\']\.["\']v["\']\.|["\']ass["\']\.).{0,20}'
vararr=['$_GET','$_POST','$_REQUEST','$_SESSION','$_SERVER']

def Check(filestr,filepath):
    if 'eval' in filestr or 'assert' in filestr:
        result = re.compile(rule).findall(filestr)
        if len(result)>0:
            for group in result:
                for var in vararr:
                    if var in group[2]:
                        return result,'eval|assert'
                resultson = re.search('\\'+group[2]+rule2,filestr)
                try:
                    if len(resultson.groups())>0:
                        return ((resultson.group(),),(result[0][0],)),'eval|assert($a)'
                except:
                    continue

        else:
            result = re.compile(rule1).findall(filestr)
            if len(result)>0:
                return result,'eval|assert(base64)'
    return None
