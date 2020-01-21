import requests
import pickle

text = requests.get("http://www.pythonchallenge.com/pc/def/banner.p").content
print(pickle.loads(text))
for list in pickle.loads(text):
    print(''.join(l[0] * l[1] for l in list))


# http://www.pythonchallenge.com/pc/def/channel.html