haystack = "hello"
needle = "ll"
k=len(needle)
for i in range(len(haystack)-k+1):
    string=""
    for j in range(i,i+k):
        string+=haystack[j]
    if needle==string:
        print(i)
else:
    print("-1")