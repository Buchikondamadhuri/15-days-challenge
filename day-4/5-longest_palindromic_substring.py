s="cbbd"
subs=[]
ans=""
for i in range(len(s)):
    sub=""
    for j in range(i,len(s)):
        sub+=s[j]
        if len(sub)>1:
           subs.append(sub)
for i in subs:
    if i==i[::-1]:
        if len(ans)<len(i):
            ans=i
print(ans)