rats=int(input("enter no of rats: "))
units=int(input("enter required unit for a rat: "))
houses=list(map(int,input().split()))
req_units=rats*units
count=0
for i in houses:
    req_units-=i
    count+=1
    if req_units<=0:
        break
print(count)