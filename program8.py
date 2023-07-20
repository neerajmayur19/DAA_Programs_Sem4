def request_allocation(requests):
    requests.sort(key = lambda x:x[1])
    n = len(requests)
    
    dp = [0]*(n+1)
    for i in range(1,n+1):
        j = i - 1
        while j>=0 and requests[j][1]>requests[i-1][0]:
            j = j-1
            dp[i] = max(requests[i-1][2]+dp[j+1],dp[i-1])
    return dp[n]


requests = [(1,2,100),(2,5,200),(3,6,300),(4,8,400),(5,9,500),(6,10,100)]
max_profit = request_allocation(requests)
print(max_profit)
