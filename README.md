# 这是一个基于python代码控制浏览器（谷歌）访问fofa从而得到相应资产IP的爬虫脚本

## 这个脚本的好处是相较于传统的爬虫更加隐蔽毕竟是操作浏览器的而且较于fofa的api接口查询更便捷更直观
 
 ## 以下是使用教程：

### 1.下载需要的模块

pip install -r requirements.txt

### 2.更改代码

chrome_options.add_argument("--user-data-dir=更改成你的谷歌浏览器用户数据路径") --> C:\\Users\\(用户名)\\AppData\\Local\\Google\\Chrome\\User Data（这是我的）

也可以在谷歌浏览器的url搜索框输入 chrome://version/ 个人资料路径  格式同上（因为避免转义）

### 3.启动谷歌浏览器的调试模式

打开cmd的管理员模式输入命令"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 

此时应该会弹出谷歌浏览器

端口可以更改同时代码也要更改

chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:端口")

（但是不建议哈 我试过几次失败了）

### 4.浏览器配置

（1）保证fofa是登录状态

（2）在显示资产数量设置为50个

![{5442B977-1A94-46EA-8F18-5FA982F1517C}](https://github.com/user-attachments/assets/b861dabf-2d20-4575-b469-d4c66a53f084)


这个在最后再说为什么

### 5.运行程序

cmd的管理员模式：

(1) python fofa.py

(2) 请输入fofa语句：

(3) 请输入次数：（这个就是尽可能的多拿ip但是重复多次其实没有多多少）

正常运行成功后会生成ip_list.txt (这就成功了)


#### 解释一下浏览器配置的问题 

这个脚本其实就是浏览器用代码的方式来运行的 登录其实也可以但没必要而其还涉及到验证码识别 不如直接手动登录了 

为什么要设置为50页？ 

因为它不能翻页也不能用文本输入来切换页数 我已经试过好办法了都没用 所以这个脚本就是每次都访问一页一页50个ip 重复次数其实就是输入相同的fofa语句再次查询找到新的ip就添加进去

我这个算个一举两得了本来普通用户一次就只能查大概60个IP 而且也解决翻不了页的问题😁

我其实可以指一条明路让会员级别的人能查到更多的资产毕竟会员一次能查询的资产比我们普通人多

https://fofa.info/result?qbase64=YXBwPSJteXNxbCI%3D&page=2&page_size=10

https://fofa.info/result?qbase64=YXBwPSJteXNxbCI%3D&page=5&page_size=10

其实每一页的url没啥变化就是page后面的参数变量所以只要每次访问的url变化就可以实现更多的ip资产但是我没钱你懂的

##### 如果有人借我会员我可以更加完善哦

### 最后
 
 看到这个项目的应该都是学安全的 有群希望大佬来指导

qq：3241986481



 





