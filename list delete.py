#Deleting element from list in python example
my_list =["zero","one","two","three","four"];
print("Elements of th list, my_list are:");
for ml in my_list:
    print(ml);
index =input("\nEnter index no:");
index=int (index);
print("Deleting the element present at index number ",index);
del my_list[index];
print("\nNow elements of the list ,my_list are:");
for ml in my_list:
    print(ml);
    print()
    print()
    print()
