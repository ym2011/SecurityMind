1.1.安全编码规范 
公开的安全编码规范参考：OWASP Secure Coding Practice  

1.2.IDE代码检测插件： 
Java编码规范方面的插件：P3C IDE 
Java漏洞检测方面的插件：Findbugs及继任者Spotbugs 
.NET漏洞检测方面的插件：Puma Scan 
支持C/C++的插件：cppcheck  

1.3.开源组件安全扫描（OSS）工具： 
OSS方面的商业产品：BlackDuck

源授权协议合规检查产品：FOSSology 
组件漏洞检查方面的开源产品：Dependency-Check（可以结合maven或Jenkins使用） 
组件漏洞检测产品：synk（可以扫描node.js nmp、ruby、java依赖中的漏洞） 
依赖方面的安全检查最为丰富的是SourceClear公司的：EFDA   

1.4.安全过滤库&中间件： 
常见的java安全过滤库：ESAPI 
Node.js的web安全过滤库可以参考：egg-security 
浏览器端的过滤库有：DOMPurify  

1.5.安全编译检查： 
通过Visual studio编译选项中的/GS选项检查缓冲区溢出，/guard:cf选项检查控制流安全。 
iOS APP安全编译选项有-fobjc-arc、-fstack-protector-all、-pie   

2.安全测试阶段 
自动化安全测试，自动化安全测试又包括静态应用安全测试（SAST）、动态应用安全测试（DAST）、交互应用安全测试（IAST）

2.1.静态应用安全测试，即对应用进行白盒测试： 
商业产品有：Fortify、奇安信代码安全卫士 
开源PHP源代码漏洞扫描产品：RIPS、progpilot 
针对Python、Ruby、Go语言的安全扫描的综合工具：huskyCI 
针对java的安全扫描工具主要有：spotbugs以及相关插件fb-contrib、find-sec-bugs
针对C/C++的安全扫描综合工具：flawfinder 
支持多种语言的综合安全扫描工具：Infer
静态应用安全测试的综合平台：SonarQube   

2.2.动态应用安全测试，即对应用进行黑盒测试： 
商业产品有：AWVS、AppScan、绿盟漏洞扫描器 
开源产品有：Arachni 
针对REST API自动化测试的产品：Astra 
针对Web Service进行安全测试的产品：WSSAT 
针对Android的开源DAST测试产品：Qark   

2.3.交互应用安全测试，作用于应用内部的安全漏洞测试： 
商业产品有：Synopsys Seeker、Veracode、CxIAST 
针对PHP的开源产品有：PHP taint、PHP Aspis 
针对Java的开源产品有：security_taint_propagation   

2.4.人工安全测试，代码审计和模糊测试： 
人工代码审计：OWASP代码审计指南 
针对协议的常用模糊测试工具：Peach fuzzer（可以对各种文件和协议进行黑盒测试） 
针对二进制漏洞的模糊测试工具有：Asan、Tsan、Msan、UBsan 
开源的Fuzz测试平台有：OSS-Fuzz   

2.5.web安全测试： 
web安全测试：OWASP安全测试指南
主要使用的工具：BurpSuite、Fiddler  

2.6.移动安全测试 
移动安全测试：OWASP移动安全测试指南 
开源的产品有：MobSF 
Android人工测试的工具有：Drozer、AppUse、Xposed、Frida 
ios人工测试的工具有：needle、iOSSecAudit  