num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
 
if (num2 < num1) and (num3 < num1):
   largest = num1
elif (num1 < num2) and (num3 < num2):
   largest = num2
else:
   largest = num3
 
print("The largest number is",largest)
