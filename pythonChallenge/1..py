## 对下面的文字进行
instr = "abcdefghijklmnopqrstuvwxyz"
outstr = "cdefghijklmnopqrstuvwxyzab"
strans = str.maketrans(instr,outstr)

test = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print(test.translate(strans))


# http://www.pythonchallenge.com/pc/def/map.html
print("map".translate(strans))

# 下一个链接为：http://www.pythonchallenge.com/pc/def/ocr.html