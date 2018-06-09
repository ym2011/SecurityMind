#!/usr/bin/python2.7
#!coding=utf-8

import os
import sys
import time
import shutil

plusarr=[] #插件列表
backdoor_count=0

def loadplus():
    for root,dirs,files in os.walk("plus"):
        for filespath in files:
            if filespath[-3:] == '.py':
                plusname = filespath[:-3]
                if plusname=='__init__':
                    continue
                __import__('plus.'+plusname)
                plusarr.append(plusname)

def Scan(path):
    loadplus() #动态添加插件
    global backdoor_count
    for root,dirs,files in os.walk(path):
        for filename in files:
            f=filename.split(".")
            c=""
            for i in range(len(f)):
                if i==0:
                    pass
                else:
                    c=c+"."+f[i]
            suffix = c.lower()
            if '.php' in suffix or '.jsp' in suffix:
                filepath = os.path.join(root,filename)
                if os.path.getsize(filepath)<500000:
                        for plus in plusarr:
                            file= open(filepath,"rb")
                            filestr = file.read()
                            file.close()
                            result = sys.modules['plus.'+plus].Check(filestr,filepath)

                            if result!=None:
                                
                                print u'FilePath: ',
                                print filepath
                                print u'describe: ',
                                print result[1]
                                print u'code: ',
                                for code in result[0]:
                                    print code[0][0:100]
                                print u'time: '+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(filepath)))+'\n\n'
                                backdoor_count= backdoor_count+1
                                '''
                                将疑似木马文件，copy到一个文件夹内。

                                '''
                                try:
                                    if os.path.exists("./ScanResult"):
                                        pass
                                    else:
                                        os.system("mkdir ScanResult")

                                    file_path="./ScanResult/"+filepath    ##file path

                                    file_dire=os.path.dirname(file_path)

                                    try:
                                        os.makedirs(file_dire)
                                    except:
                                        pass

                                    shutil.copyfile(filepath,file_path)
                                except:
                                    print 'Permission denied'
                                    
                                break

def ScanFiletime(path,times):
    global backdoor_count
    times = time.mktime(time.strptime(times, '%Y-%m-%d %H:%M:%S'))
    print '########################################'
    print 'FilePath           time   \n'

    for root,dirs,files in os.walk(path):
        for curfile in files:
            f=curfile.split(".")
            c=""
            for i in range(len(f)):
                if i==0:
                    pass
                else:
                    c=c+"."+f[i]

            suffix = c.lower()
            filepath = os.path.join(root,curfile)
            if '.php' in suffix or '.jsp' in suffix:
                FileTime =os.path.getmtime(filepath)
                if FileTime>times:
                    backdoor_count +=1
                    print filepath+'        '+ time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(FileTime))

if __name__ == "__main__":
    print '----------------------------------------'
    print """
          ╭╮　　　　　　　╭╮　　
       　││　　　　　　　││　　
       ╭┴┴———————┴┴╮
       │　　　　　　　　　　　│　　　
       │　　　　　　　　　　　│　　　
       │　●　　　　　　　●　│
       │○　　╰┬┬┬╯　　○│
       │　　　　╰—╯　　　　│　
       ╰——┬Ｏ———Ｏ┬——╯
       　 　╭╮　　　　╭╮　　　　
       　 　╰┴————┴╯
----┏━☆━━━━━━━━━━━━┓----
----┃ MaskFindShell 1.0          ┃----
----┃ Author:nmask               ┃----
----┃ SITE:thief.one             ┃----
----┗━━━━━━━━━━━━━━┛----
    """

    if len(sys.argv)!=3 and len(sys.argv)!=2:
        print '【Error】'
        print 'style1: '+sys.argv[0]+' filepath'
        print 'style2: '+sys.argv[0]+' filepath time(Forexample:"2013-09-09 12:00:00")'
        sys.exit()
       
    if os.path.lexists(sys.argv[1])==False:
        print '【Error Tag】：not found file---'
        sys.exit()

    if len(sys.argv)==2:
        print '\n\n【Start】'
        print sys.argv[1]+'\n'
        Scan(sys.argv[1])
        print '【End】'
        print '\tsum number: '+str(backdoor_count)
    else:
        print '\n\n【Start】'
        print sys.argv[1]+'\n'
        ScanFiletime(sys.argv[1],sys.argv[2])
        print '\n【End】'
        print '\tsum number: '+str(backdoor_count)
