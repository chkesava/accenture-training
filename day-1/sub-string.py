s=input()
length=len(s)
count=0
for i in range(length):
    for j in range(i,length):
        print(s[i:j+1])
        count+=1
print(count)
