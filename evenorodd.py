 num = int(input("Enter any number: "))
flag = num%2
if flag == 1:
    print(num, "is an odd number")
elif flag == 0:
    print(num, "is an even number")
else:
    print("Error, Invalid input")
