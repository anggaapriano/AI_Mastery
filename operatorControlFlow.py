#OPERATORS
#Arithmetic Operators (+,-,*,/,%,//,**)
a = 5
b = 2
print(a, '+', b, "=", a+b)
print(a, '-', b, "=", a-b)
print(a, '*', b, "=", a*b)
print(a, '/', b, "=", a/b)
print(a, '%', b, "=", a%b)
print(a, '//', b, "=", a//b)
print(a, '**', b, "=", a**b)

#Comparision Operators (>,<,==,>=,<=,!=)
a = 5
b = 2
print(a, '>', b, "=", a>b)
print(a, '<', b, "=", a<b)
print(a, '==', b, "=", a==b)
print(a, '>=', b, "=", a>=b)
print(a, '<=', b, "=", a<=b)
print(a, '!=', b, "=", a!=b)

#Logical Operators (and,or,not)
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

#Identity Operators (is, is not)
a = 5
b = 5
print(a is b)
print(a is not b)

#Membership Operators (in, not in)
a = "Hello World"
print('H' in a)
print('hello' not in a)

#CONTROL FLOW
#Conditional Statement (if, if - else, if - elif - else, nested if - else)
mobilA = 150
if mobilA <= 150:
    print("Saya beli kontant")
elif mobilA > 150 and mobilA <= 190:
    print("Saya beli kredit")
else :
    print("Saya tidak beli")

#user defined functions
def show_words(data = "default"):
    return(data)
print(show_words())

