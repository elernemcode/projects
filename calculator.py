print("1.+")
print("2.-")
print("3.x")
print("4.÷")

op = input("Enter the number of operation that you want to do: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if op == "1":
    print(num1 + num2)
elif op == "2":
     print(num1 - num2)
elif op == "3":
     print(num1 * num2)
elif op == "4":
    print(num1 / num2)
else:
    print("infalid operation")