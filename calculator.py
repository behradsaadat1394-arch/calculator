operator = input("enter operator(+,-,*,%): ")
number1 = float(input("enter the 1st number: "))
number2 = float(input("enter the 2nd number: "))
if operator == "+":
    result = number1 + number2
    print (round(result , 0))
elif operator == "-":
    result = number1 - number2
    print (round(result , 0))
elif operator == "*":
    result = number1 * number2
    print (round(result , 0))
elif operator == "%":
    result = number1 % number2
    print (round(result , 0))
else:
    print ("f{operator}isn't a valed operator")
