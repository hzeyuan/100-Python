import requests
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=77864"
text = requests.get(url).text

for i in range(400):
    number_list = re.findall("\d+", text)
    if len(number_list) == 1:
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + number_list[0]
    elif len(number_list) == 0:
        number = url.split('nothing=')[1]
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(int(number) / 2)
    elif len(number_list) == 2:
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + number_list[0]
        content = requests.get(url).text
        if content.find("You've been misleaded to here.") != -1:
            print("正确数字为{}".format(number_list[1]))
            url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + number_list[1]
    r = requests.get(url)
    if r.status_code == 200:
        text = r.text
        print(str(i) + ": ", text)

# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831的下一个答案：peak.html