numbers=[2,7,11,15]
target=9
l=0
r=len(numbers)-1
while l<r:
    summ=numbers[l]+numbers[r]
    if summ==target:
        print(l+1,r+1)
        break
    elif summ<target:
        l+=1
    else:
        r-=1


    
