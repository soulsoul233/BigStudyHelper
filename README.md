# BigStudyHelper
江西财经大学青年大学习小工具

## 注意
⚡本项目仅供学习参考, "学习新思想,争做新青年", 请大家自觉按时完成大学习!!

⚡⚡本项目不会记录你的任何信息,所有信息均储存在你的计算机中

⚡⚡⚡最新更新本地版,将userID以及name保存在本地,除进行学习外不会上传任何信息,更安全!

⚡⚡⚡⚡请不要向任何人泄露你的userID,因为其他人可能伪造你的身份登录校园网其他网站

### 本地版使用方法

+ clone本项目,本地版位于"Local"目录下或至[release](https://github.com/FupengWang/BigStudyHelper/releases)界面下载编译好的exe文件
+ 打开'setting.config'文件,修改name为你的中文真实姓名,url为从微信"青年大学习"中复制出来的链接,样例可参考默认配置文件
+ clone项目的同志请自行将源代码封装成系统服务项(NSSM);下载编译好的同志请将exe设置成启动项(创建快捷方式,将快捷方式移动到'启动'目录下)


### 云函数版使用方法
1,请在'BigStyduHelper.py'第64行至第67行中填入你的姓名与userID信息,支持多人,注意格式.

2,userID是从微信"青年大学习"界面中提取出来的一段形为 "http://onestop.jxufe.edu.cn/eos/wx/youthStudy/studyList.jsp?userId=xxxxxxxxxxxxx" 的网址中xxxxxxxxxxxxx的一部分字符串,通常是以"=="或者"%3D%3D"结尾,请将它填写到代码的相应位置

3,如需要启用钉钉群通知请修改'BigStyduHelper.py'第61行与第62行的钉钉机器人配置信息.

若不填写,则不会开启钉钉群通知,仅本地控制台输出执行结果


### 自动签到

配置GitHub Action或者腾讯云函数即可实现自动签到

建议执行周期为四天

腾讯云函数入口为main_handler
