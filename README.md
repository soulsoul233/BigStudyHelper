# BigStudyHelper
江西财经大学青年大学习小工具

## 注意
⚡本项目仅供学习参考, "学习新思想,争做新青年", 请大家自觉按时完成大学习!!

⚡⚡本项目不会记录你的任何信息,所有信息均储存在你的计算机中

⚡⚡⚡请不要向任何人泄露你的userID,因为其他人可能伪造你的身份登录校园网其他网站


### 使用方法
1,请在'BigStyduHelper.py'第64行至第67行中填入你的姓名与userID信息,支持多人,注意格式.

2,userID是从微信"青年大学习"界面中提取出来的一段形为 "http://onestop.jxufe.edu.cn/eos/wx/youthStudy/studyList.jsp?userId=xxxxxxxxxxxxx" 的网址中xxxxxxxxxxxxx的一部分字符串,通常是以"=="或者"%3D%3D"结尾,请将它填写到代码的相应位置

3,如需要启用钉钉群通知请修改'BigStyduHelper.py'第61行与第62行的钉钉机器人配置信息.

若不填写,则不会开启钉钉群通知,仅本地控制台输出执行结果


### 自动签到

配置GitHub Action或者腾讯云函数即可实现自动签到

建议执行周期为四天

腾讯云函数入口为main_handler
