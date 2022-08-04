# Kali Linux 安装英伟达显卡驱动和CUDA套件     // Debian // Ubuntu

## 1. 检查仓库源

确保仓库包含`contrib`和`non-free`部分。Kali默认就有此部分。`Debian`可能需要自己手动添加，建议检查下为好。

- 检查是否包括`contrib`和`non-free`
  
  ```bash
  grep "contrib non-free" /etc/apt/sources.list
  ```

- 如果没有的话，需要手动添加。源文件在`/etc/apt/sources.list`
  
  ```bash
  apt edit-sources
  或
  vim /etc/apt/sources.list
  ```

- 更新软件包
  
  ```bash
  apt update && apt full-upgrade -y
  ```

## 2. 检查显卡

查看显卡信息和驱动信息。

```bash
┌──(root㉿kali)-[~]
└─# lspci | grep -i vga
09:00.0 VGA compatible controller: NVIDIA Corporation GP106 [GeForce GTX 1060 6GB] (rev a1)

┌──(root㉿kali)-[~]
└─# lspci -s 09:00.0 -v
09:00.0 VGA compatible controller: NVIDIA Corporation GP106 [GeForce GTX 1060 6GB] (rev a1) (prog-if 00 [VGA controller])
        Subsystem: ZOTAC International (MCO) Ltd. GP106 [GeForce GTX 1060 6GB]
        Flags: bus master, fast devsel, latency 0, IRQ 80, IOMMU group 15
        Memory at f6000000 (32-bit, non-prefetchable) [size=16M]
        Memory at e0000000 (64-bit, prefetchable) [size=256M]
        Memory at f0000000 (64-bit, prefetchable) [size=32M]
        I/O ports at e000 [size=128]
        Expansion ROM at 000c0000 [disabled] [size=128K]
        Capabilities: [60] Power Management version 3
        Capabilities: [68] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [78] Express Legacy Endpoint, MSI 00
        Capabilities: [100] Virtual Channel
        Capabilities: [250] Latency Tolerance Reporting
        Capabilities: [128] Power Budgeting <?>
        Capabilities: [420] Advanced Error Reporting
        Capabilities: [600] Vendor Specific Information: ID=0001 Rev=1 Len=024 <?>
        Capabilities: [900] Secondary PCI Express
        Kernel driver in use: nouveau
        Kernel modules: nouveau


┌──(root㉿kali)-[~]
└─# 
```

> - 对于笔记本电脑或者迷你主机等有集成显卡的设备。主显示卡或许使用的是集成显卡，那么在`lspci | grep -i vga`这一步就不会显示`nvidia`独显。下面命令可以查看主显示卡是哪一个。
>   
>   ```bash
>   kali@kali:~$ lspci | grep -i vga
>   00:02.0 VGA compatible controller: Intel Corporation HD Graphics 620 (rev 02)
>   ```
> 
> - 为了查看`nvidia`显卡，可以安装`nvidia-detect`，并运行此软件。
>   
>   ```bash
>   ┌──(root㉿kali)-[~]
>   └─# apt install nvidia-detect
>   
>   ┌──(root㉿kali)-[~]
>   └─# nvidia-detect 
>   Detected NVIDIA GPUs:
>   09:00.0 VGA compatible controller [0300]: NVIDIA Corporation GP106 [GeForce GTX 1060 6GB] [10de:1c03] (rev a1)
>   
>   Checking card:  NVIDIA Corporation GP106 [GeForce GTX 1060 6GB] (rev a1)
>   Uh oh. Failed to identify your Debian suite.
>   ```

## 3. 安装

- 上一步检查出来的信息中，`Kernel driver in use`和`Kernel modules`显示的是`nouveau`。说明现在使用的是开源通用驱动，而我们现在要安装`nvidia`闭源驱动和`CUDA`套件。
  
  ```bash
  apt install -y nvidia-driver nvidia-cuda-toolkit
  ```

- 安装过程中会提示以下信息
  
  ```bash
  ─────────────────────────────────┤ Configuring xserver-xorg-video-nvidia ├─────────────────────────────────┐
  │                                                                                                           │
  │ Conflicting nouveau kernel module loaded                                                                  │
  │                                                                                                           │
  │ The free nouveau kernel module is currently loaded and conflicts with the non-free nvidia kernel module.  │
  │                                                                                                           │
  │ The easiest way to fix this is to reboot the machine once the installation has finished.                  │
  │                                                                                                           │
  │                                                  <Ok>                                                     │
  │                                                                                                           │
  └───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
  ```

- 重启电脑
  
  ```bash
  reboot
  ```

## 4. 确认

检查`nvidia`驱动和`CUDA`套件是否安装成功。

```bash
┌──(root㉿kali)-[~]
└─# nvidia-smi   
Thu Aug  4 23:29:36 2022       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.129.06   Driver Version: 470.129.06   CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:09:00.0  On |                  N/A |
|  0%   55C    P0    33W / 190W |    396MiB /  6075MiB |      1%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1078      G   /usr/lib/xorg/Xorg                191MiB |
|    0   N/A  N/A      1474      G   xfwm4                               2MiB |
+-----------------------------------------------------------------------------+


┌──(root㉿kali)-[~]
└─# lspci | grep -i vga
09:00.0 VGA compatible controller: NVIDIA Corporation GP106 [GeForce GTX 1060 6GB] (rev a1)

┌──(root㉿kali)-[~]
└─# lspci -s 09:00.0 -v
09:00.0 VGA compatible controller: NVIDIA Corporation GP106 [GeForce GTX 1060 6GB] (rev a1) (prog-if 00 [VGA controller])
        Subsystem: ZOTAC International (MCO) Ltd. GP106 [GeForce GTX 1060 6GB]
        Flags: bus master, fast devsel, latency 0, IRQ 86, IOMMU group 15
        Memory at f6000000 (32-bit, non-prefetchable) [size=16M]
        Memory at e0000000 (64-bit, prefetchable) [size=256M]
        Memory at f0000000 (64-bit, prefetchable) [size=32M]
        I/O ports at e000 [size=128]
        Expansion ROM at 000c0000 [virtual] [disabled] [size=128K]
        Capabilities: [60] Power Management version 3
        Capabilities: [68] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [78] Express Legacy Endpoint, MSI 00
        Capabilities: [100] Virtual Channel
        Capabilities: [128] Power Budgeting <?>
        Capabilities: [420] Advanced Error Reporting
        Capabilities: [600] Vendor Specific Information: ID=0001 Rev=1 Len=024 <?>
        Capabilities: [900] Secondary PCI Express
        Kernel driver in use: nvidia
        Kernel modules: nvidia
```

> 查看显卡详细信息，例如温度、转速、内存占用等。
> 
> ```bash
> nvidia-smi -i 0 -q
> ```
