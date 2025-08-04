strs=["eat","tea","tan","ate","nat","bat"]
dici={}
for i in strs:
    key="".join(sorted(i))
    if key not in dici:
        dici[key]=[i]
    else:
        dici[key].append(i)
print(list(dici.values()))
