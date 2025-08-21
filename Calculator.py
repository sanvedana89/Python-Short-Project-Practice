x = float(input("Enter number 1: "))
y = float(input("Enter number 2: "))
Cal = input("Enter operation name (add, subtract, multiply, divide): ")
if Cal == "add" or Cal == "+":
    ans = x + y
elif Cal == "subtract" or Cal == "-":
    ans = x - y
elif Cal == "multiply" or Cal == "*":
    ans = x * y
elif Cal == "divide" or Cal == "/":
    if y != 0:
        ans = x / y
else:
    ans = "Invalid operation."

print("Result:", ans)
