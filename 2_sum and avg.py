'''sum and avg of 3 numbers'''

a,b,c=[float(x)for x in input("Enter 3 numbers:").split()]
sum=a+b+c
avg=sum/3
print("the sum is%i\naverage is%.2f"%(sum,avg))
