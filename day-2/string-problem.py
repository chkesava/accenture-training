s=input()
count=0
final=""
for i in s:
    if i =="-":
        count+=1
    else:
        final+=i
print("-"*count+final)
   