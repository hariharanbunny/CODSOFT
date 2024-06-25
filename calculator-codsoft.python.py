
count=0

while(count==0):
    print("Select an operation to perform : ")
    print("1. ADD")
    print("2. SUBSTRACT")
    print("3. MULTIPLICATION")
    print("4. DIVISION")

    print("Enter the operation number to be performed:")
          
    operation = input()
    if operation == "1":
        print("Performing addition:")
        num1 = input("Enter first number : ")
        num2 = input("Enter second number : ")
        print("The Sum is "+ str(int(num1) + int(num2)))

    elif operation == "2":
        print("Performing substaction:")
        num1 = input("Enter first number : ")
        num2 = input("Enter second number : ")
        print("The Difference is "+ str(int(num1) - int(num2)))

    elif operation == "3":
        print("Performing multiplication:")
        num1 = input("Enter first number : ")
        num2 = input("Enter second number : ")
        print("The Product is "+ str(int(num1) * int(num2)))

    elif operation == "4":
        print("Performing division:")
        num1 = input("Enter first number : ")
        num2 = input("Enter second number : ")
        print("The Division is "+ str(int(num1) / int(num2)))

    else:
         print("INVALID ENTRY")

    count=int(input("press 0 to try again , press 1 to exit"))
if count == 1:
    print("Thank you")
else:
    print("Invalid entry")


