#  Write python program that swap two number with temp variable and without temp variable.

# Python program to swap two variables with temp vaeiable

# To take inputs from the user

x = input('Enter value of x: ')
y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

# Python program to swap two variables with temp vaeiable

x = input('Enter value of x: ')
y = input('Enter value of y: ')

x,y=y,x
print("x=",x)
print("y=",y)