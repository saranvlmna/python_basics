num1= input("Input first number ")
num2 = input("Input second number ")
num3 = input("Input third number ")

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
     return num1
    elif num2 >= num1 and num2 >= num3:
       return num2
    else:
       return num3

largest_num=max_num(num1,num2,num3)
print(largest_num)
  
