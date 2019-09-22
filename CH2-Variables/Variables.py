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