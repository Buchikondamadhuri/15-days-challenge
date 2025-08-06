nums=[-1,0,3,5,9,12]
target=2
i=0
j=len(nums)-1
while i<j:
    if nums[i]==target:
        print(i)
        break
    elif nums[j]==target:
        print(j)
        break
    else:
        i+=1
        j-=1
else:
    print("-1")