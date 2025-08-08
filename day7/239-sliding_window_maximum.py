nums=[1,3,-1,-3,5,3,6,7]
k=3
ans=[]
temp=[]
for i in range(len(nums)):
    temp.append(nums[i])
    if len(temp)==k:
        ans.append(max(temp))
        temp.pop(0)
print(ans)
        


