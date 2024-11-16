def solution(arr):
    if not arr and len(arr)<2:
        return False
    min_price=float('inf')
    profit=0
    for price in arr:
        min_price=min(min_price,price)
        profit=max(profit,price-min_price)
    return profit
arr=list(map(int,input().split()))
print(solution(arr))



