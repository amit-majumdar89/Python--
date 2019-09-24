#
# Declare & Initialize A Variable
#

a = 1
print(a)

#
# Redeclare & Reinitialize A Variable
#

a = "Redclared \"A\" "
print(a)

#
# ERROR: Variables of different types cannot be combined
#

print('ERROR: Variables of different types cannot be combined')
print('Hence \"A String Type\" + 123 does not work')
print('Type cast to str(123) works in this case')

a = "A String type" + str(123)

#
# Global VS Local Variables in functions
#

f = "A Global Variable"

def someFunction():
    f = "A Local Variable"
    print(f)
    
someFunction()
print(f)
print('Both the copies of \'f\' have different variables \'f\' declared inside \'someFunction()\' has its own scope hence both are two seperate variables.')

print('To make the variables inside the def as global. Declare as \'global\' like: \'g\' ')

g = 1

def anotherFunction():
    global g
    g = 10
    print(g)

anotherFunction()
print(g)

print('del deletes the defination hence will throw an exception')
del g
# print(g)

#
# Variable Types
#

#
# Numbers
#

print('******** Numbers ********')

floatVar = 3.16
print(floatVar)

intVar = 3
print(intVar)

print('Python supports two types of numbers - integers and floating point numbers. (It also supports complex numbers)')

#
# String (Strings are defined either with a single quote or a double quotes.)
#

print('Strings are defined either with a single quote or a double quotes.')

stringVarWithDoubleQuotes = "stringVarWithDoubleQuotes"
stringVarWithSingleQuotes = 'stringVarWithSingleQuotes'

print(stringVarWithSingleQuotes)
print(stringVarWithDoubleQuotes)

print('The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)')

print("Don't worry about apostrophes")

#
# Assignments can be done on more than one variable "simultaneously" on the same line like this
#

a1 , b1 = 4, 5
print(a1)
print(b1)