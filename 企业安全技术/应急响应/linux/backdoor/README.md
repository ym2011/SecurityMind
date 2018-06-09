## scaing-backdoor


Webshell扫描工具，通过各种规则和算法实现服务器脚本后门查杀。

目前已实现功能：

+ 根据关键字静态扫描webshell


### 使用说明

    ➜  python scan.py -h
    scan usage:
    简单使用：scan.py filepath
    -h,--help: 获取帮助信息.
    -v, --version: 获取scan版本
    -p,--path: 指定将要扫描的路径
    -l,--low: 系统/数据库弱密码扫描

### TODO

+ 文件大小判断（可配置选项）
+ 支持多命令选项
+ 动态扫描
+ 十六进制度读取文件
+ 提取webshell关键字
+ 弱密码提示/潜在威胁提示
+ 提供多系统支持
+ 特征库包含各种木马/病毒/文件路径/cms/shell/框架信息等特征码为各个平台提供特征码支持
