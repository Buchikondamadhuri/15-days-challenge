prices=[7,1,5,3,6,4]
profit=0
minval=prices[0]
for i in range(1,len(prices)):
    profit=max(profit,prices[i]-minval)
    minval=min(minval,prices[i])
print(profit)