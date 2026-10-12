# Platform: Custom | Link: N/A
text1 = input("Enter text: ")

text2 = input("Enter text: ")



dic1 = {}

dic2 = {}



for i in text1:

    if i in dic1:

        dic1[i]+=1

    else:

        dic1[i]=1



for i in text2:

    if i in dic2:

        dic2[i]+=1

    else:

        dic2[i]=1



if dic1 == dic2:

    print("Anagram")



else:

    print("Not anagram")
