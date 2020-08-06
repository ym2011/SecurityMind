# 1. 代码安全检查
## 1.1 IDE代码检测插件  
Java编码规范方面的插件：P3C IDE
Java漏洞检测方面的插件：Findbugs及继任者Spotbugs
.NET漏洞检测方面的插件：Puma Scan
支持C/C++的插件：cppcheck

## 1.2 开源组件安全扫描（OSS/SCA）工具  
组件漏洞检查方面的商业产品：   
OSS方面的商业产品：BlackDuck    
FOSSology，开源授权协议合规检查产品    
snyk，可以扫描node.js nmp、ruby、java依赖中的漏洞，协议授权安全，多平台集成；链接：https://snyk.io/     
JFrog Xray，安全漏洞及依赖分析平台；链接：https://www.jfrogchina.com/xray/      
组件漏洞检查方面的开源产品：     
Dependency-Check（可以结合maven、Jenkins、sonar使用）；链接：https://github.com/jeremylong/DependencyCheck   
陌陌安全 MOSEC-X-PLUGIN 系列插件开源；链接：https://www.anquanke.com/post/id/212553   
snyk，可以扫描node.js nmp、ruby、java依赖中的漏洞，协议授权安全，多平台集成；链接：https://snyk.io/       

## 1.3 安全过滤库&中间件：
常见的java安全过滤库：ESAPI
Node.js的web安全过滤库可以参考：egg-security
浏览器端的过滤库有：DOMPurify

## 1.4 安全编译检查：
通过Visual studio编译选项中的/GS选项检查缓冲区溢出，/guard:cf选项检查控制流安全。
iOS APP安全编译选项有-fobjc-arc、-fstack-protector-all、-pie

# 2. 应用安全测试产品
安全测试阶段，自动化安全测试，自动化安全测试又包括静态应用安全测试（SAST）、动态应用安全测试（DAST）、交互应用安全测试（IAST）  
## 2.1 静态应用安全测试，即对应用进行白盒测试    
### 商业产品有：
Fortify：静态代码扫描工具；地址：http://www.fortify.net/   
Checkmarx：静态代码工具；地址：https://www.checkmarx.com/   
奇安信代码安全卫士， 地址：https://www.codesafe.cn/     
### 开源产品：  
开源PHP源代码漏洞扫描产品：  
RIPS：用于PHP脚本漏洞的静态源代码分析器：地址：http://rips-scanner.sourceforge.net   
progpilot 
开源Python 源代码扫描产品：  
OpenStack Bandit：基于Python AST的静态分析器，用来查找Python代码中存在的通用安全问题的工具。地址：https://github.com/openstack/bandit/releases/   

开源的Java源代码漏洞扫描产品：  
banruo：基于的fotify的自动化代码审计系统。地址:https://github.com/yingshang/banruo   
Find Security Bugs： 用于Java Web应用程序的安全审计。地址：(https://find-sec-bugs.github.io/  
spotbugs以及相关插件fb-contrib、Raptor、

多种语言的源代码扫描产品
Cobra：一款源代码安全审计工具，支持检测多种开发语言源代码中的大部分显著的安全问题和漏洞。地址：https://github.com/WhaleShark-Team/cobra      
VCG:一种用于C++、C语言、VB、PHP、Java和PL/SQL的自动代码安全审查工具。地址：https://sourceforge.net/projects/visualcodegrepp/   
Hades：静态代码脆弱性检测系统。地址：https://github.com/zsdlove/Hades 
Infer
SonarQube  
Seay源代码审计系统
huskyCI：针对Python、Ruby、Go语言的安全扫描的综合工具     
flawfinder：针对C/C++的安全扫描综合工具：     

## 2.2 动态应用安全测试，即对应用进行黑盒测试   
商业产品：AWVS、AppScan、Netspark、绿盟漏洞扫描器RSAS、启明天镜漏洞扫描
开源产品：Xray、gaby、Owasp ZAP、Arachni   
针对REST API自动化测试的产品：Astra   
针对Web Service进行安全测试的产品：WSSAT   
针对Android的开源DAST测试产品：Qark   

## 2.3 交互应用安全测试，作用于应用内部的安全漏洞测试   
商业产品：
国内：默安-雳鉴IAST、新思Seeker软件、开源网安SecZone VulHunter、墨云VackBot、悬镜灵脉 AI-IAST渗透测试平台   
国外：Contrast Security、Veracode、CxIAST   
开源：百度RASP、PHP taint、PHP Aspis、security_taint_propagation（JAVA）


# 3. 综合安全测试   
## 3.1 web业务安全测试：   
web安全测试：OWASP安全测试指南   
主要使用的工具：BurpSuite、Fiddler   
## 3.2 移动业务安全测试
移动安全测试：OWASP移动安全测试指南   
开源的产品有：MobSF   
Android人工测试的工具有：Drozer、AppUse、Xposed、Frida   
ios人工测试的工具有：needle、iOSSecAudit   

## 3.3人工安全测试，代码审计和模糊测试：
人工代码审计：OWASP代码审计指南
针对协议的常用模糊测试工具：Peach fuzzer（可以对各种文件和协议进行黑盒测试）  
针对二进制漏洞的模糊测试工具有：Asan、Tsan、Msan、UBsan   
开源的Fuzz测试平台有：OSS-Fuzz   
