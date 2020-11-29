def getText():
    txt=input("请输入一段字符串")
    txt= txt.lower()
    for ch in '!@#$%^&*()_+~{}|:"<>?' :
        txt=txt.replace(ch,"")
    return txt
hamletTxt= getText()
words=list(hamletTxt)
counts={}
for word in words:
     if word==" ":
        continue
     else:
         counts[word] =counts.get(word,0)+1
items =list(counts.items())
items.sort(key=lambda x :x[1],reverse=True)
for i in range (5):
    word,count= items[i]
    print("{0:<10}{1:>5}".format(word,count))