# ChatGPT 中文提示词

## 起因

[ChatGPT Desktop](https://github.com/lencx/ChatGPT) 导入自定义提示词需要csv格式或json格式，而 [PlexPt](https://github.com/PlexPt)/**[awesome-chatgpt-prompts-zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)** 中的提示词写在Markdown文件中，因此就让 ChatGPT 写一个Python脚本将 Markdown 文件转换为 csv 文件，转换前先手动将无关内容剔除，然后根据 Markdown 语法提取提示词。

![](https://github.com/muxinxy/ChatGPT-Prompts-ZH/raw/main/20230224235156.png)

## 文件

- md2csv.py: Python 脚本

- prompts-zh.md: 原 Markdown 文件

- prompts-zh.csv: csv文件转换结果

- md2csv.md: 让ChatGPT写脚本的过程

## 感谢

[PlexPt/awesome-*chatgpt*-prompts-zh](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)
