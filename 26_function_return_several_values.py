def fv(n1,n2):
    a=n1+n2
    b=n1-n2
    c=n1*n2
    d=n1/n2
    return a,b,c,d
n1=float(input("Enter the value of n1:"))
n2=float(input("Enter the value of n2:"))
Ar=fv(n1,n2)
print(Ar)
for i in Ar: print(i)