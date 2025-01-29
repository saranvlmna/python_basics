num1= input("Eneter a number: ")
num2= input("Entor another number: ")
operation=input("Enter operation: ")

if operation=="+":
 result = float(num1) + float(num2)

elif operation=="*":
 result = float(num1) * float(num2)

elif operation=="-":
 result = float(num1) - float(num2)

elif operation=="/":
 result = float(num1) / float(num2)

else:
 result = "Invalid operation"
print(result)