#!/usr/bin/python2.7
#coding:utf-8

import re

keywords=[
            '启动自动攻击',
            'xxddos',
            'phpddos',
            'fsockopen("udp:',
            'fsockopen("tcp:',
            '$_get["moshi"]=="udp"'
        ]


#此插件白名单列表 (['文件路径'],['误报特征码'])
whitefilter=[
                (['install/svinfo.php'],['fsockopen("tcp:']),
]


def Check(filestr,filepath):

    filestr = filestr.lower()

    #纯关键词查找-暂不确定后门
    for key in keywords:
        if key in filestr:
            isok=1
            for white in whitefilter:
                if white[0][0] in filepath.replace('\\','/') and white[1][0] in key:
                    isok=0
            if isok:
                return ((key,),),'PHP ddos_cc'
    return None
