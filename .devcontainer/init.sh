#!/bin/bash

# 添加alias
echo 'source /workspaces/AskBQ/.devcontainer/alias' >> ~/.bashrc

# 安装常用工具
sudo apt-get update
sudo apt-get install -y vim

# 安装requirements.txt
pip install -r requirements.txt
