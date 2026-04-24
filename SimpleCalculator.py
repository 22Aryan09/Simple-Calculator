def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def mult(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
    else:
        return" Error ! Division by zero"

print('Simple Calculator')
print('CHoose operation')
print('1.Addition')
print('2.Substraction')
print('3.Multiplication')
print('4.Division')

choice=input('Enter choice(1/2/3/4):')

num1=float(input('Enter first number'))
num2=float(input('Enter second number'))

if choice=='1':
    print('Result',add(num1,num2))
elif choice=='2':
    print('Result',substract(num1,num2))
elif choice==3:
    print('Result',mult(num1,num2))
elif choice==4:
    print('Result',divide(num1,num2))
else:
    print("Invalid choice")