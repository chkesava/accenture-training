def validateString(string,n):
    if n<4:
        return 0
    if string[0].isdigit():
        return 0
    cap=0
    num=0
    for i in range(n):
        if string[i]==" " or string[i]=="/":
            return 0
        
string=input()
n=int(input())
print(validateString(str))