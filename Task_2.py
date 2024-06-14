#Function to add
def add(num1,num2):
    return num1 + num2

#Function to subtract
def subtract(num1,num2):
    return num1 - num2

#Function to multiply
def mul(num1,num2):
    return num1 * num2

#Function to divide
def divide(num1,num2):
    return num1 / num2


print("**********Start Menu**********\n" \
      "1.Addition\n" \
      "2.Substraction\n" \
      "3.Multiply\n" \
      "4.Divide\n")

select = int(input("Select a operation: "))

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if select == 1:
    print(num1 ,"+ ",num2,"= ",add(num1,num2))

elif select == 2:
    print(num1,"- ", num2,"= ",subtract(num1,num2))

elif select == 3:
    print(num1,"* ",num2,"= ",mul(num1,num2))

elif select == 4:
    print(num1,"/",num2,"= ",divide(num1,num2))

else:
    print("Invalid number!")






