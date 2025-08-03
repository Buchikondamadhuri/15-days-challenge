nums=[1,2,3,4]
ans=[1]*len(nums)#[1,1,1,1]
for i in range(1,len(nums)):
    ans[i]=ans[i-1]*nums[i-1]
r=1
for i in range(len(nums)-1,-1,-1):
    ans[i]*=r
    r*=nums[i]
print(ans)
