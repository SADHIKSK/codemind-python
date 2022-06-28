n=int(input())
oc=0
ec=0
arr=list(map(int,input().split()))
for i in range(n): 
    if arr[i]%2==0:
        ec+=1
    else:
        oc+=1
print(ec,oc)