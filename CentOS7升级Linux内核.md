# CentOS 7 升级Linux内核

> Upgrade Kernel on CentOS 7

运行的一些程序可能会对`Linux`内核版本有要求，本文介绍如何升级`CentOS 7`的内核。

## 1. 查看系统信息

- 查看发行信息
  
  ```bash
  cat /etc/os-release
  ```

- 查看`CentOS`版本
  
  ```bash
  cat /etc/redhat-release
  ```

- 查看内核版本
  
  ```bash
  uname -r
  ```

## 2. 更新源并升级

```bash
yum update -y
```

> 如有必要可换源。

## 3. 启用并安装ELRepo仓库

- 导入ELRepo仓库的公钥信息
  
  ```bash
  rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
  ```

- 安装ELRepo
  
  ```bash
  yum install https://www.elrepo.org/elrepo-release-7.el7.elrepo.noarch.rpm
  ```

## 4. 查看可用内核

```bash
yum list available --disablerepo='*' --enablerepo=elrepo-kernel
```

> 其中包括了主线版本`kernel-ml`和长期支持版本`kernel-lt`。

## 5. 升级到最新内核

```bash
yum --enablerepo=elrepo-kernel install kernel-ml -y
```

> 也可升级到最新的长期支持版本的内核（版本号低于上述主线版本）：
> 
> ```bash
> sudo yum --enablerepo=elrepo-kernel install kernel-lt -y
> ```

## 6. 设置grub

- 查看grub配置信息
  
  ```bash
  awk -F\' ' $1=="menuentry " {print i++ " : " $2}' /etc/grub2.cfg
  ```

- 设置新的内核为`grub2`默认版本
  
  ```bash
  grub2-set-default 0
  ```

## 7. 重启服务器并检查内核版本

- 重启服务器
  
  ```bash
  reboot
  ```

- 检查内核版本
  
  ```bash
  uname -r
  ```

- 禁止`elrepo`仓库
  
  进入目录`/etc/yum.repos.d`，将文件`elrepo.repo`中`[elrepo]`区块下的`enabled`修改为`0`。
  
  ```bash
  enabled=0
  ```
  
  > 不禁止也可以，更新系统的时候会稍慢点。

- 安装`epel`源
  
  ```bash
  yum install epel-release -y 
  ```
  
  > 用来安装`htop`等程序。
