import re

first = "90052.txt"
while True:
    with open("./channel/" + first, "r") as t:
        text = t.readline()
        answer = re.findall("\d+", text)
        if len(answer) == 1:
            first = answer[0] + ".txt"
            print("path:{} and text:{}".format(first, text))
        else:
            print(first)
            print(text)
            break
# Collect the comments.
import zipfile
first = "90052.txt"
file = zipfile.ZipFile('./channel.zip', 'r')
print(file)
while True:
    line = str(file.read("%s" % first))
    m = re.search("\d+", line)
    print(file.getinfo("%s" % first).comment.decode("utf-8"), end="")
    if m is None:
        print(file.getinfo("%s" % first).comment.decode("utf-8"))
        break

    first =  m.group(0)+".txt"
