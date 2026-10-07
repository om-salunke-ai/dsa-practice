# Platform: Custom | Link: N/A
text = input("Enter text: ").lower()
dic = {}
for i in text:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
