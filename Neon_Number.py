n =int(input())
sq=n*n
s=0
while sq:
    s+=sq%10
    sq//=10
if s==n:
    print('Neon Number')
else:
    print('Not Neon Number')