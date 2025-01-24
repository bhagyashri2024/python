no=int (input("enter the number"))
numbers=[23,33,45,65,22,88,44,67,70]

for i in numbers:
    if(i==no):
        print ("number found in the list ")
        break
else:
    print("number not found in the list")
