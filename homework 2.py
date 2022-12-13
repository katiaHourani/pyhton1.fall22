# homework 2 template
# beginning python course
# name:katia hourani 

def multiply(a,b):
    ''' 
    multiples two numbers
    
    inputs: 
        a, b (number): inputs
    
    returns (number): product of a and b
    '''
    m=a*b
    print(m)
    return m

a = 5.2
b = 5.3
multiply(a,b)


def absolute(x):
#    '''
#    compute the absolute value of a number. note that you cannot use the abs() function.

#    inputs:
#        n (number): operand

#    returns (number): the magnitude of the input
#    '''
    if x<0:
        print("x is negative")
        print(-x)
        return x
    elif x>0:
        print("x is positive")
        print(x)
        return x
    elif x==0:
        print("x is null")
        print(x)
        return x
    
absolute( -5)


def prime(n):
    ''' 
    tests if a number is prime and returns a boolean value. no built-in functions can be used

    inputs: 
        n (number): the input
    
    returns (boolean): whether or not the number is prime 
    '''
    n=int(n)
    if n <= 1:
        return False
    else:
         for i in range(2,round((n**(1/2)))):
             if (n% i == 0):
               return False
         else:
                return True
    
print(prime(input("enter a prime number.")))

       



def list_loop(lst):
    '''
    Given a list of integers and a variable, write a loop 
    to count the number of values in the list that are strictly 
    greater than val. 
    
    For example, given the list [-1, -2, -3, -4] and 0 for val, 
    the result would be zero because there are no values that are
    strictly greater than zero in the list.

    Inputs:
        lst (list): list of integers
        var (number): variable 
    

    Returns (number): number of values in lst strictly greater than val
    '''  
    v=float(input("enter a number"))  
    x = [item for item in lst if item>v]
    #value of x
    len(x)
    print(len(x))
    
   
lst=[2,3,4,5,6,7]

list_loop(lst)



def list_prod(lst):
    '''
    Given a list compute the product of the numbers in the list
    
    Inputs:
        lst (list): list of numbers
    
    Returns (number): product of values in list
    '''
    product = 1

    for item in lst:
         product = product * item
        
         print(product)

lst=[2,3,4,5]
list_prod(lst)



