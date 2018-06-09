##工具简介
findWebshell是一款基于python开发的webshell检查工具，可以检查任意类型的webshell后门。

##使用说明
    Usage: main.py [options]

    Options:
      -h, --help            show this help message and exit
      -p PATH, --path=PATH  input web directory filepath
      -o OUTPUT, --output=OUTPUT
                            create a html report
      -e php|asp|aspx|jsp|all, --ext=php|asp|aspx|jsp|all
                            define what's file format to scan

示例
    
    python main.py -e php -p /var/www/test -o output
    -e 网页格式
    -p 扫描的路径
    -o 生成的html文件名，默认生成report.html

##开发文档
###字典添加
- directory目录下的sensitiveWord.py定义的是后门中的敏感关键字，可以手动添加，格式为{"关键字":"类型"}

```
php_sensitive_words = {
    "www.phpdp.org":"PHP神盾加密后门",
    "www.phpjm.net":"PHP加密后门"
}
```

- directory目录下的webshell.py定义的是webshell列表，直接添加webshell到列表里
```
php_webshell = [
"后门.php",
"xxoo.php",
"一句话.php"
]
```
###插件开发
- 命令规范

插件命名格式：网页类型_后门类型-plugin.py

**示例**
```
php_eval_assert-plugin.py
php_preg_replace-plugin.py
asp_execute-plugin.py
```
- 函数规范和返回值

函数格式

    def judgeBackdoor(fileCtent)
    成功返回后门类型，失败返回None

**示例**
```
def judgeBackdoor(fileCtent):
	if keyword in fileCtent:
		result = re.compile(rule).findall(fileCtent)
		if len(result) > 0:
			return  backdoorType
	else:
		return None
```

[插件规则参考](http://www.oschina.net/p/seayfindshell)
