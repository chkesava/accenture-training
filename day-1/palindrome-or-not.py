number=int(input())
temp=number
rev_num=0
while temp>0:
    rev_num=rev_num*10+(temp%10)
    temp=temp//10
if rev_num==number:
    print("palindrome")
else:
    print("not a palindrome ")
