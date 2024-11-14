string=input()
n=len(string)
res=int(string[0])
for i in range(1,n-1,2):
    if string[i]=="A":
        res&=int(string[i+1])
    else:
        res