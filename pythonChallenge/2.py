import requests
import re

content = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html').text
anwser = re.sub('\n|\t|\r', '', content)  # 去除一些空格
anwser = re.findall("find.*?<!--(.*?)-->", anwser)  # 取出注释
anwser = list(str(anwser))  # 转化为列表
key = (s for s in anwser if s.isalpha()) #找到里面的字母
print("".join(key))
# 结果 equality
