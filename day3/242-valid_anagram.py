s="abcc"
t="abca"
dici1={}
dici2={}
for i in s:
    if i not in dici1:
        dici1[i]=1
    else:
        dici1[i]+=1
for i in t:
    if i not in dici2:
        dici2[i]=1
    else:
        dici2[i]+=1
for i,j in dici1.items():
    if j!=dici2[i]:
        print("Not an anagram")
        break
else:
    print("Valid anagram")
    



        