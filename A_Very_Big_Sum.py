n=int(input())
sum=0
arr=list(map(int,input().split()))
for i in range(n):
    sum+= arr[i]
print(sum)