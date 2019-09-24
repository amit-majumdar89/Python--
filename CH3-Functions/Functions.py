#
# Functions (definations) Starts with teh keyword 'def' like def functionName:
#

def greet():
    print('Hello Amit, Good Morning')
    
greet()

#
# Functions With Parameters:
#
def greet(name, message):
    print (message + " " + name)
    
greet(name = 'Tom', message = "Howdy!")

def add(num1, num2):
    print(num1 + num2)

add(5, 5)

#
# Functions With Parameters and a Return Type:
#
def square(x):
    return x * x

print(square(5))

# A simple Python function to check 
# whether x is even or odd

def checkIfEvenOrOdd(x):
    if (x % 2 == 0): 
        print("Its Even")
        return True
    else:
        print("Its Odd")
        return False

print(checkIfEvenOrOdd(2))
print(checkIfEvenOrOdd(3))

# One important thing to note is, in Python every variable name is a reference. 
# When we pass a variable to a function, a new reference to the object is created. 
# Parameter passing in Python is same as reference passing in Java.

def swap(x, y):
    temp = x
    x = y
    y = temp

x = 12
y = 90

swap(x, y)
print(x)
print(y)

# Default arguments:
# A default argument is a parameter that assumes a default value if a 
# value is not provided in the function call for that argument.The following example illustrates Default arguments.

def sayHello(name, message = "Hello"):
    print(message + " " + name)

sayHello(name = "Amit")

# Keyword arguments:
# The idea is to allow caller to specify argument name with values
#  so that caller does not need to remember order of parameters.

def saveName(firstname, lastname):
    return firstname + " " + lastname

print(saveName(firstname = "Tom", lastname = "Holland"))

# Variable length arguments:
# We can have both normal and keyword variable number of arguments. Please see this for details.

def printValues(*argv):
    for arg in argv:
        print(arg)
        

printValues(2, 3, 'Hello', 90, 100)

# Python program to illustrate 
# *kargs for variable number of keyword arguments 

def myFun(**kwargs): 
	for key, value in kwargs.items(): 
		print ("%s == %s" %(key, value)) 

# Driver code 
myFun(first ='Geeks', mid ='for', last='Geeks')	 

# Anonymous functions: In Python, anonymous function means that a function is without a name.
# As we already know that def keyword is used to define the normal functions and
# the lambda keyword is used to create anonymous functions. Please see this for details.

# Python code to illustrate cube of a number 
# using labmda function 
	
cube = lambda x: x*x*x 
print(cube(7)) 

# Python code to illustrate square of a number 
# using labmda function 

square = lambda x: x*x
print(square(16))

# Python code to get full name
# using labmda function with multiple arguements

fullName = lambda firstName, middleName, lastName: firstName + " " + middleName + " " + lastName
print(fullName(firstName= "Keth", middleName= "Medley", lastName= "Hedger"))

pii = lambda: 3.14

print(pii())