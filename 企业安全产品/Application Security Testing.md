# 1. 代码安全检查

## 1.1 IDE代码检测插件  
Java编码规范方面的插件：P3C IDE
Java漏洞检测方面的插件：Findbugs及继任者Spotbugs
.NET漏洞检测方面的插件：Puma Scan
支持C/C++的插件：cppcheck

## 1.2 开源组件安全扫描（OSS/SCA）工具  
### 组件漏洞检查方面的商业产品：   
Black Duck® 软件组件分析 (SCA)：应用和容器开源风险、授权协议合规；链接：https://www.synopsys.com/zh-cn/software-integrity/security-testing/software-composition-analysis.html   

奇安信开源卫士：开源组件资产识别、安全风险分析、授权协议合规等功能；链接：https://www.qianxin.com/product/detail/pid/13   

棱镜七彩FossEye：开源软件的选型、安全研发、安全检测、持续集成、持续部署等开源软件安全合规解决方案，链接：https://www.7-cai.com/fosseye.html 

snyk，可以扫描node.js nmp、ruby、java依赖中的漏洞，协议授权安全，多平台集成；链接：https://snyk.io/ 

JFrog Xray，安全漏洞及依赖分析平台；链接：https://www.jfrogchina.com/xray/     

### 组件漏洞检查方面的开源产品：     
Dependency-Check（可以结合maven、Jenkins、sonar使用）；链接：https://github.com/jeremylong/DependencyCheck 

snyk开源版本， 可以扫描node.js nmp、ruby、java依赖中的漏洞，协议授权安全，多平台集成，需要登录注，授权后使用，在IDEA直接继承使用；链接：https://snyk.io/    

陌陌安全 MOSEC-X-PLUGIN 系列插件开源；链接：https://www.anquanke.com/post/id/212553   


## 1.3 安全过滤库&中间件：
常见的java安全过滤库：OWASP ESAPI    

Node.js的web安全过滤库可以参考：egg-security 

浏览器端的过滤库有：DOMPurify 

陌陌安全JAVA、PHP SDK开源；链接：https://security.immomo.com/blog/94   

## 1.4 安全编译检查：
通过Visual studio编译选项中的/GS选项检查缓冲区溢出，/guard:cf选项检查控制流安全。
iOS APP安全编译选项有-fobjc-arc、-fstack-protector-all、-pie

# 2. 应用安全测试产品
安全测试阶段，自动化安全测试，自动化安全测试又包括静态应用安全测试（SAST）、动态应用安全测试（DAST）、交互应用安全测试（IAST）  
## 2.1 静态应用安全测试

也称代码安全审计，即对应用进行白盒测试，也可以人工+工具结合方式进行  。

### 源代码安全审计商业产品有：
Fortify：静态代码扫描工具；地址：http://www.fortify.net/  

Checkmarx：静态代码工具；地址：https://www.checkmarx.com/ 
奇安信代码安全卫士， 地址：https://www.codesafe.cn/     

### 源代码安全审计开源产品：  
RIPS：用于PHP脚本漏洞的静态源代码分析器：地址：http://rips-scanner.sourceforge.net   
progpilot：针对 PHP 的白盒审计框架，基于 PHP-CFG 来实现控制流图 (CFG) 、PHP-Parser 来实现抽象语法书 ( AST 树) 的生成；网址：https://github.com/designsecurity/progpilot   
OpenStack Bandit：基于Python AST的静态分析器，用来查找Python代码中存在的通用安全问题的工具。地址：https://github.com/openstack/bandit/releases/   
banruo：Java源代码漏洞，基于的fotify的自动化代码审计系统。地址:https://github.com/yingshang/banruo   
Find Security Bugs： 用于Java Web应用程序的安全审计。地址：(https://find-sec-bugs.github.io/  
Cobra：针对PHP、Java、Python 等开发语言进行代码安全审计，还支持对 WEB 框架的识别，更新截止2018年4月。地址：https://github.com/WhaleShark-Team/cobra  
Cobra-W，Cobra-W是从Cobra2.0发展而来的分支，将工具重心从尽可能的发现威胁转变为提高发现漏洞的准确率以及精度。网址：https://github.com/LoRexxar/Kunlun-M   
Infer facebook开源的一款静态代码扫描工具，针对Java, C++, Objective-C, and C 语言，网址：https://github.com/facebook/infer/  
Hades：静态代码脆弱性检测系统。地址：https://github.com/zsdlove/Hades

SonarQube  CI/CD集成平台的代码安全扫描  

VCG:一种用于C++、C语言、VB、PHP、Java和PL/SQL的自动代码安全审查工具。地址：https://sourceforge.net/projects/visualcodegrepp/  

Seay源代码审计系统 国人开发的多语言的代码安全审计产品  

huskyCI  针对Python、Ruby、Go语言的安全扫描的综合工具   

flawfinder 针对C/C++的安全扫描综合工具  

spotbugs以及相关插件fb-contrib、Raptor  

## 2.2 动态应用安全测试

即对应用进行黑盒测试，即常规的web漏洞扫描     

### 商业产品：

AWVS、AppScan、Netspark、绿盟漏洞扫描器RSAS、启明天镜漏洞扫描

### 开源产品：

Xray、gaby、Owasp ZAP、Arachni   

针对REST API自动化测试的产品：Astra   
针对Web Service进行安全测试的产品：WSSAT   
针对Android的开源DAST测试产品：Qark   

## 2.3 交互应用安全测试

作用于应用内部的安全漏洞测试，即测试、开发人员也进行参与   

### 商业产品：
国内：默安-雳鉴IAST、新思-Seeker软件、开源网安-SecZone VulHunter、、悬镜-灵脉AI-IAST渗透测试平台   
国外：Contrast Security、Veracode、CxIAST   

### 开源产品：

百度RASP、PHP taint、PHP Aspis、security_taint_propagation（JAVA）

## 2.4自动化渗透测试

模拟黑客或者渗透测试人员，自动化对站点进行渗透测试。

### 商业产品：
国内：墨云-VackBot、悬镜-灵脉PTE、四维创智-天象综合渗透测试平台、四维创智-小智-智能渗透测试机器人、
国外：metasploit pro, canvas  
### 开源产品：

# 3. 综合安全测试   
## 3.1 web业务安全测试：   
web安全测试：OWASP安全测试指南   
主要使用的工具：BurpSuite、Fiddler   

## 3.2 移动业务安全测试
移动安全测试：OWASP移动安全测试指南   
### 开源的产品有

MobSF   

Android人工测试的工具有：Drozer、AppUse、Xposed、Frida   
ios人工测试的工具有：needle、iOSSecAudit   

## 3.3人工安全测试

渗透测试人员或者代码审计人员对应用进行代码审计和模糊测试：

人工代码审计：OWASP代码审计指南
针对协议的常用模糊测试工具：Peach fuzzer（可以对各种文件和协议进行黑盒测试）  
针对二进制漏洞的模糊测试工具有：Asan、Tsan、Msan、UBsan   
开源的Fuzz测试平台有：OSS-Fuzz   


# 4 SDL安全开放流程管理平台



# 5.devsecops平台
