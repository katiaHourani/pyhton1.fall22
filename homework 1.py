# Homework 1 Part 2 Template
# Beginning Python Course
#name:Katia Hourani8


def add(a,b):
    ''' 
    Returns the sum of a and b
    
    Inputs: 
        a, b (number): inputs
    
    Returns (number): sum of a and b
    '''
    sum= a+b
    print(a,"+",b,"=",sum)
    return sum #return value
num1=float(input("input the first number: ")) #input from user for num1
num2=float(input("input the  second  number :")) #input from user for num2
add(num1,num2)

def strictly_increasing(n1,n2,n3,n4):
    ''' 
    Returns true if the numbers are strictly increasing in magnitude
    (if |n4| > |n3| > |n2| > |n1|), false otherwise 

    Inputs:
        n1, n2, n3, n4 (numbers): inputs

    Returns (Boolean): true if the arguments are strictly increasing in magnitude, false otherwise
    '''
    if w>z>y>x:
        return True 
    else : return False
n1=float(input("input the first number :"))
n2=float(input("input the second number :"))
n3=float(input("input the third number :"))
n4=float(input("input the forth number :"))
x=abs(n1)
y=abs(n2)
z=abs(n3)
w=abs(n4)
print("are the numbers stricktly increasing?",strictly_increasing(x,y,z,w) )


def area(b, h):
    '''
    Returns the area of the triangle
    
    Inputs:
        b (number): base
        h (number): height
    
    Returns (number): Area of the triangle
    '''
    n=2
    f_n=float(n)
    a=(b*h)/f_n
    print("the area of the triangle is:", a)
    return a
b= float(input("enter your base:"))
h= float(input("enter your height"))

area(b,h)

def remainder(p, q):
    '''
    Returns the remainder of p divided by q (p/q).
    
    Inputs:
        p, q (integers): inputs
        
    Returns (integer): remainder of p / q '''
    if q>0:

        s=p%q
        print("the remainder is", s)
    else: 
        print( "invalid");

p=int(input("enter an integer"))
q=int(input("enter a positive number"))

remainder (p,q)
    