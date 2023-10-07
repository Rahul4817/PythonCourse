n1 = int(input("Enter a first number:"))
n2 = int(input("Enter a second number"))

print("press 1 for additoin,n\ press 2 for subtration n\ press 3 for multiply n\ press 4 for division")


choice =int(input("Enter a your choice number 1-4:"))

if choice == 1:

    sum = n1+n2
    print(sum)

elif choice == 2:
    sub = n1-n2
    print(sub)

elif choice == 3:
    mul=n1*n2
    print(mul)

elif choice == 4:
    div = n1/n2
    print(div)


