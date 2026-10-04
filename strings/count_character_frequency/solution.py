text = input("Enter text: ")
dic = {}
for i in text:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

print(dic)
