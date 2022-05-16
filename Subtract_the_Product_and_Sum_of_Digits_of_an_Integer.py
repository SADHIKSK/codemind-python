n=int(input())
s=0
p=1
while(n):
    p*=n%10
    s+=n%10
    n//=10
print(p-s)