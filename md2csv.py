import re
import csv

# 读取 README.md 文件
with open("prompts-zh.md", "r", encoding="utf-8") as file:
    data = file.read()

# 用正则表达式找到所有的标题和引用
pattern = re.compile(r'##\s*(.*?)\n\s*>\s*(.*?)\n', re.DOTALL)
matches = pattern.findall(data)

# 去除标题和引用文本中的多余空格，并使用 csv.writer 写入 csv 文件
with open("prompts-zh.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow(['act', 'prompt'])  # 写入标题行
    for act, prompt in matches:
        writer.writerow([act.strip(), prompt.strip()])
