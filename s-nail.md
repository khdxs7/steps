# 渗透之命令行发送邮件 // s-nail //

> 可用于各种条件触发时发送邮件提醒。

## 一、获取邮箱授权码

qq邮箱授权码获取

- 登录`qq`邮箱

- 点击`设置`

- 点击`账户`选项卡

- 下翻条目至`POP3/IMAP/SMTP/Exchange/CardDAV/CalDAV服务`
  
  - 开启`MAP/SMTP服务`-->验证密保
  
  - 获取授权码
  
  - （可选）勾选`SMTP发信后保存到服务器`

## 二、安装配置s-nail

### 1. 安装软件

```bash
apt update && apt install s-nail
```

### 2. 配置SMTP

在文件`/etc/s-nail.rc`末尾添加以配置信息：

```bash
vim /etc/s-nail.rc
```

```vim
###########################################
#################SMPT配置###################
###########################################

set v15-compat        #版本所必须，v15版本的配置格式
set smtp-auth=login   #验证方式为登录

###########################################
#设置发件人，昵称<邮箱完整格式>
set from="KHDXS7<3049261332@qq.com>"  

#配置发送邮件服务器，SSL加密，端口465或587。
#设置smtp服务器端口为465
#用户名为QQ号，密码为授权码

#端口465设置
set mta=smtps://3049261332:aujsycdczdopdfie@smtp.qq.com:465 

#端口587设置（备用）
#set smtp-use-starttls
#set mta=smtp://username:password@smtp.qq.com:587

###########################################
#常用联系人
#alias 别名 邮箱

#Loop,邮件可以自己发送给自己
alias qq 3049261332@qq.com

#常用联系人1
#alias name1 123456789@mailserver.com
#常用联系人2
#alias name2 123456789@mailserver.com
#常用联系人3
#alias name3 123456789@mailserver.com
```

## 三、发送邮件

### 1. 普通发送邮件

- 发送文本
  
  ```bash
  echo "正文" | s-nail -s "主题" 收件人
  ```
  
  ```bash
  echo "TEST" | s-nail -s "Mail from KALI" qq
  ```

- 发送附件
  
  ```bash
  echo "正文" | s-nail -s "主题" -a ./附件 收件人
  ```
  
  ```bash
  echo "TEST" | s-nail -s "Attachment from KALI" -a ./attachment.txt qq
  ```

### 2. 应用举例

- 任务结束提醒

- 任务结果通知

- 监测状态变动通知（比如监测tcp连接，靶机上线提醒等）

###### 以`nmap`为例，将扫描结果发送到邮箱。

```bash
nmap -p- -sV -sC -O -oN nmap.txt 192.168.1.150 | s-nail -s "Output of Nmap" qq
```
