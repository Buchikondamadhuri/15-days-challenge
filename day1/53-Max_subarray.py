nums=[5,4,-1,7,8]
max_sum=float('-inf')
##bruteforce
'''
for i in range(len(nums)):
    for j in range(i,len(nums)):
        summ=0
        for k in range(i,j+1):
            summ+=nums[k]
        max_sum=max(summ,max_sum)
print(max_sum)'''
##optimal-kadane's algorithm
summ=0
for i in nums:
    summ+=i
    max_sum=max(summ,max_sum)
    if summ<0:
        summ=0
print(max_sum)

    
        
        
    
    