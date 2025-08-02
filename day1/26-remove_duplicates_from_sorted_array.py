nums = [1,1,2]
i=0
for j in range(len(nums)):
    if nums[j]!=nums[i]:
        nums[i+1]=nums[j]
        i+=1
print(i+1)
print(nums)