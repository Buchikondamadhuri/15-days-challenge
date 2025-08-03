def isPalindrome(s):
    s2=""
    for i in s:
        if i.isalnum():
            s2+=i.lower()
    l=0
    r=len(s2)-1
    while l<r:
        if s2[l]!=s2[r]:
            return False
        else:
            l+=1
            r-=1
    return True
s="A man,a plan, a canal: Panama"
print(isPalindrome(s))