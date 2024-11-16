number_1=int(input())
number_2=int(input())
count=0
while number_1>0 and number_2>0:
    if (number_1%10)+(number_2%10)>9:
        if len(str(number_1))!=1 and len(str(number_2))!=1:
            count+=1
    number_1//=10
    number_2//=10
    number_2+=1
print(count)
