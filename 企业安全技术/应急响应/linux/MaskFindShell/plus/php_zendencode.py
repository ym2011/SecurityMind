#encoding:utf-8
import re
import os

def Check(filestr,filepath):

    #php zend一句话  caidao.php
    if filestr[:4]=='Zend':
        if os.path.getsize(filepath)==178:
            return (('Zend Encode',),),'zend'

        #其他后门判断c
        return None
