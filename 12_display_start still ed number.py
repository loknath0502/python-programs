n,m=[int(i)for i in input("Enter start value,stop value:").split(" ")]
x=n
if x%2!=0: x=n+1
while(x<=m):
    print(x)
    x+=2
m=int(input())        #1
n=int(input())        #50