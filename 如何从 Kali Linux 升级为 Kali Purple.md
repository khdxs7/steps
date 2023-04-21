# 如何从 Kali Linux 转换为 Kali Purple

## 一、升级 kali linux 到最新版本

### 1. 检查源

最新版`Kali Linux`和`Kali Purple`都是基于`Debian 12`的`Linux`发行版，软件源中应该包含有`non-free-firmware`。若没有，则需手动添加。

腾讯源：

```bash
deb http://mirrors.tencent.com/kali kali-rolling main contrib non-free non-free-firmware
```

## 2. 更新kali

更新软件库并升级软件。

```bash
apt update && apt full-upgrade -y
```

### 3. 检查是否需要重启

```bash
[ -f /var/run/reboot-required ] && reboot
```

## 二、升级到 kali purple

### 1. 安装purple相关程序

```bash
apt install kali-tools-identify kali-tools-detect kali-tools-protect kali-tools-recover kali-themes-purple -y
```

### 2. 重装系统菜单

```bash
apt reinstall kali-menu 
```

### 3. 重启系统

```bash
reboot
```
