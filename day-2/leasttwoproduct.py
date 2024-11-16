
def leasttwoproduct(n,arr,temp):
    if n<2:
        return -1
    arr.sort()
    product=arr[0]*arr[1]
    if product<temp:
        return product
    else:
        return 0
n=int(input())
arr=list(map(int,input().split()))
temp=int(input())
print(leasttwoproduct(n,arr,temp))