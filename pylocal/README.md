# 基于python的本地逻辑验证

## 环境准备

## Vscode 类开发者

如果已经你已经基于devcontainer.json配置了devcontainer，那么你已经准备好了环境。

如果还没有，请下载dev container

## 其他开发者

V1版本可以用conda类环境，或者直接python3.12环境。去安装依赖。

`pip install -r requirements.txt`即可

## 开始使用

step1: 加密保存key
step2: 使用功能

加密的目的只要是防止使用者的key被编辑器读取到明文，然后泄漏。

1. 生成加密密钥：`python encrypt.py init`
2. 输入自己的openai的key或者deepSeek的key `python encrypt.py encrypt "your-api-key-here"`
3. 解密key验证是否正确：`python encrypt.py decrypt`。其他库调用这个decrypt方法
4. 更换自己的真实key

## 核心例子

[挑战](/doc/challenges/README.md)