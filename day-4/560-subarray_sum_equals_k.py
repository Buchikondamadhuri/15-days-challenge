nums=[1,2,3]
k=3
prefix_sum={0:1}
curr_sum=0
count=0
for i in range(len(nums)):
    curr_sum+=nums[i]
    if (curr_sum-k) in prefix_sum:
        count+=prefix_sum[curr_sum-k]
    if curr_sum not in prefix_sum:
        prefix_sum[curr_sum]=0
    prefix_sum[curr_sum]+=1   
print(count)
     
           
        

        