for i in range(1,6):
    for j in range(1,6):
        if (i<=5):
            if(j<=i):
                print(j,end="")
        print (end="")
    print()


for i in range (1,6):
    for j in range(1,6):
        if(i<=5):
            if(j<=i):
                print("*",end="")
        print (end="")
    print()


i=5
while i>=1:
    j=1
    while j<=i:
        print (i,end="");
        j=j+1
    i=i-1
    print()
    
