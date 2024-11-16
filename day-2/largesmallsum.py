def LargeSmallSum(arr):
    if len(arr)==0:
        return 0
    if len(arr)<=3:
        return 0
    even_nums=[]
    odd_nums=[]
    for i in range(len(arr)):
        if i%2==0:
            even_nums.append(arr[i])
        else:
            odd_nums.append(arr[i])
    even_nums.sort()
    odd_nums.sort()
    return even_nums[-2]+odd_nums[-2]
arr=list(map(int,input().split()))
print(LargeSmallSum(arr))