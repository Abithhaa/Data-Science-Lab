x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
if x>y:
    x,y=y,x
for i in range(1,x+1):
    if x%i==0 and y%i==0:
        gcd=i
print("GCD of",x,"and",y,"is",gcd);

OUTPUT:
Enter the first number:4
Enter the second number:5
GCD of 4 and 5 is 1
