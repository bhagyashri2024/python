def factorial (n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
    
num=int(input("enter the number"))

if num<0:
    print("fractorial dosn't exists for negative number")
elif num ==0:
    print("factorial of 0 is 1")
else:
    print("factorial of ",num,"is",factorial(num))
    
