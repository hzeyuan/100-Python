import re

import requests

content = requests.get('http://www.pythonchallenge.com/pc/def/equality.html').text
notes = re.search('<!--(.*?)-->', re.sub('\n', '', content))
if notes:
    ret = re.findall('[a-z]+[A-Z]{3}([a-z])[A-Z]{3}[a-z]+', notes.group())
    print(ret)
# 答案：linkedlist