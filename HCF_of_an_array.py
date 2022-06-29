n=int(input())
arr = list(map(int,input().split()))
hcf=arr[0]
for i in range(1,n):
    while hcf!= arr[i]:
        if hcf>arr[i]:
            hcf-=arr[i]
        elif hcf<arr[i]:
            arr[i]-=hcf
print(hcf)