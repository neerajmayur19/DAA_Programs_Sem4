def knapsack(max_weight,weights,values,n):
    dp = [0 for i in range(max_weight+1)]
    
    for i in range(1,n+1):
        for w in range(max_weight,0,-1):
            if weights[i-1]<=w:
                dp[w] = max(dp[w],dp[w-weights[i-1]]+values[i-1])
    return dp[max_weight]
#Driver's Code
weight = [3,5,6,2]
values = [10,4,9,11]
max_weight = 7
print(knapsack(max_weight,weight,values,len(values)))
