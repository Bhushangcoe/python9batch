def show():
 print('hii')

show()
try:
 n1=int(input('Enter number1:'))
 n2=int(input('Enter number2:'))
 div=n1/n2
 print("Division=",div)
except ValueError:
 print("please enter numbers only")
except ZeroDivisionError:
 print('Cannot divide by zero')

print('Hello')
print("addition=",34+23)
