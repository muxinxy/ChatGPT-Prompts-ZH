import re
import csv

# 读取 awesome-chatgpt-prompts-zh.md 文件
with open("awesome-chatgpt-prompts-zh.md", "r", encoding="utf-8") as file:
    data = file.read()

# 用正则表达式找到所有的标题和引用
pattern = re.compile(r'##\s*(.*?)\n\s*>\s*(.*?)\n', re.DOTALL)
matches = pattern.findall(data)

# 去除标题和引用文本中的多余空格
matches = [(act.strip(), prompt.strip()) for act, prompt in matches]

# 将数据写入 csv 文件
with open("awesome-chatgpt-prompts-zh.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['act', 'prompt'])  # 写入标题行
    writer.writerows(matches)  # 写入所有数据行
