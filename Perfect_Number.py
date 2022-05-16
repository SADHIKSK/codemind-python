n=int(input())
s=0
x=1
while x<=n//2:
    if n%x==0:
        s+=x
    x+=1
if (s==n):
    print("True")
else:
    print('False')