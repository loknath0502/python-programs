'''using if else condition'''

a=int(input("Enter a Number:"))       
# if a%2==0:
#     print(f"{a} is Even Number")
# else:
#     print(f"{a} is odd Number")

'''separating even and odd number'''

b=int(input("Enter a Number:"))
for a in range(2,a,2):      # only Even numbers
    print(a)
    for b in range(1,b,1):   #only odd number
        print(b)
