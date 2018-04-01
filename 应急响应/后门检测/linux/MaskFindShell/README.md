# MaskFindShell
linux下webshell查杀工具

#### 参照：SeayFindShell  在此基础上添加了一些jsp的判断插件

```bash
python MaskFindShell.py   扫描目录

python MaskFindShell.py   ./test             （基于规则匹配）

python MaskFindShell.py ./test "2016-06-01 12:00:00"  （基于修改时间)
```

扫描结束后，会在当前目录下生成一个ScanResult目录，里面存放着疑似的木马文件。

#### 注意：如果程序执行失败，请检查程序权限，将该程序目录权限设置为777，即执行命令：chmod 777 MaskFindShell

by nmask 2016

