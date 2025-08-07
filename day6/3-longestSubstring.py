s="abcabcbb"
sett=set()
l=0
maxi=0
for r in range(len(s)):
    while s[r] in sett:
        sett.remove(s[l])
        l+=1
    sett.add(s[r])
    maxi=max(maxi,r-l+1)
print(maxi)
    
        

    