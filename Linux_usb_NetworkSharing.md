# Linux通过手机USB网络共享上网 // Debian // Kali // Ubuntu

> 因为各种各样的原因，Linux系统有时无法通过自身网卡接入互联网，而需要通过手机才能接入互联网。

　

### 1. 连接好数据线并在手机设置中打开“USB网络共享”

```bash
 设置 --> 个人热点 --> USB网络共享
```

### 2. 终端查看USB接口

```bash
ip addr
```

> 输出结果中会显示网络接口的名字，但是没有IP地址。（“usb0”，或者其他名字）  

### 3. 为网络接口分配IP地址

```bash
dhclient usb0
```

### 4. 确认网络接口情况

```bash
ip addr
```

> 此时，usb0应该已被分配IP地址。

### 5.确认已接入互联网

```bash
ping www.baidu.com
```


