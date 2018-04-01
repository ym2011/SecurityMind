#!/usr/bin/python2.7
#coding:utf-8

import re

rule1='(\$_(GET|POST|REQUEST)\[.{0,15}\]\s{0,10}\(\s{0,10}\$_(GET|POST|REQUEST).{0,15})'
rule2='((\$(_(GET|POST|REQUEST|SESSION|SERVER)(\[[\'"]{0,1})\w{1,12}([\'"]{0,1}\])|\w{1,10}))[\s\n]{0,20}\([\s\n]{0,20}(@{0,1}\$(_(GET|POST|REQUEST|SESSION|SERVER)(\[[\'"]{0,1})\w{1,12}([\'"]{0,1}\])|\w{1,10}))[\s\n]{0,5}\))'
rule3='\s{0,10}=\s{0,10}[{@]{0,2}(\$_(GET|POST|REQUEST)|file_get_contents|str_replace|["\']a["\']\.["\']s["\']\.|["\']e["\']\.["\']v["\']\.|["\']ass["\']\.).{0,10}'
vararr=['$_GET','$_POST','$_REQUEST','$_SESSION','$_SERVER']

#此插件白名单列表 (['文件路径'],['误报特征码'])
whitefilter=[
                (['integrate.php'],['$code ($_POST[\'cfg\'])']),
                (['Lib/Action/IntegrateAction.class.php'],['$code ($_POST[\'cfg\'])']),
                (['phpcms/modules/template/file.php'],['$_GET[\'action\']($_GET[\'html\']'])
]

def Check(filestr,filepath):
    result = re.compile(rule1).findall(filestr)
    if len(result)>0:
        isok=1
        for white in whitefilter:
            if white[0][0] in filepath.replace('\\','/') and white[1][0] in result[0][0]:
                isok=0
        if isok:
            return result,'$_GET[a]($_POST[b])'
    else:
        result = re.compile(rule2).findall(filestr)
        finalresult = result
        #print finalresult
        if len(result)>0:
            #提取变量跟踪看看是否可控，然后大一堆逻辑判断是不是后门。。。
            for group in result:
                for var in vararr:
                    if var in group[1]:
                        resultson= re.search('\\'+group[6]+rule3,filestr)
                        try:
                            if len(resultson.groups())>0:
                                isok=1
                                for white in whitefilter:
                                    if white[0][0] in filepath.replace('\\','/') and white[1][0] in result[0][0]:
                                        isok=0
                                if isok:
                                    return ((resultson.group(),),(result[0][0],)),'Danger'
                        except:
                            pass
                for var in vararr:
                    if var in group[6]:
                        resultson= re.search('\\'+group[1]+rule3,filestr)

                        try:
                            if len(resultson.groups())>0:
                                isok=1
                                for white in whitefilter:
                                    if white[0][0] in filepath.replace('\\','/') and white[1][0] in result[0][0]:
                                        isok=0
                                if isok:
                                    return ((resultson.group(),),(result[0][0],)),'Danger'
                        except:
                            pass

                result1= re.search('\\'+group[1]+rule3,filestr)
                result2= re.search('\\'+group[6]+rule3,filestr)
                try:
                    if len(result1.groups())>0 and len(result2.groups())>0:
                        isok=1
                        for white in whitefilter:
                            if white[0][0] in filepath.replace('\\','/') and white[1][0] in result[0][0]:
                                isok=0
                        if isok:
                            return ((result1.group(),),(result2.group(),),(finalresult[0][0],)),'Danger'
                except:
                    continue
                return None
        else:
            return None
