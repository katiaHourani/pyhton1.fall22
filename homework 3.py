# Katia Hourani
# HW3 Restaurant
# Welcome to Python Kitchen!
# This week you will use your newly learned knowledge of lists, tuples, dictionaries 
# and sorting to create a simulation of a restaurant. 
# Your code will be able to print menus, take orders and more. 

# Here is a list of dishes Python Kitchen provides. It is a list of tuples.
# Each tuple has information of one dish in order: (Number, Name, Price, Origin, Whether is vegetarian)
dishes=[(1,'Salmon Sushi', 30, 'Japan', False), 
        (2,'Pork Dumplings', 25, 'China', False), 
        (3,'Choziro Tacos', 20, 'Mexico', False),
        (4, 'Chickpea Curry', 36, 'India', True),
        (5, 'Apple Pie', 16, 'USA', True),
        (6, 'Jollof Rice', 18, 'Nigeria', False),
        (7, 'Dolma', 45, 'Azerbaijan', False),
        (8, 'Vegetable Pho', 25, 'Vietnam', True),
        (9, 'Kvass', 12, 'Russia',  True),
        (10, 'Luau', 30, 'Samoa', True)]

# # TODO: Put the dishes into this dictionary. The key of the dictionary is the dish's name, the value is the dish's price.
# # Example: Salmon Sushi: 30
# # USE LOOPS: Think about how you can use loops to automate this process for you instead of hardcoding all the dishes
for item in dishes:
    prices={"dish_name": item[1],
            "dish_price":item[2]
            }
    print(prices)


# TODO: -- Complete the code here --
#FUNCTIONS
#######################################################################
def print_menu (dishes):
    """
        print_menu() function should print the menu.
        
        You will iterate through the list dishes and print the dish, origin and price in a readable format. 
        If you directly print the list or the tuples, it will be too messy. 
        
        Embed it into text so you get something like: 
        Example: Sushi   origin: Japan   price: 30
    
    """
    for dish in dishes:
         print("dish name : ",dish[1],"; ","origin : ",dish[3] ,"; " , "price: ", dish[2],". ")

#######################################################################
def print_vegetarian_menu():
     """ 
         print_vegetarian_menu() function should list vegetarian options in the menu.
         this is indicated by the true/false in the last tuple of the list 'dishes'.
        
     """
     for items in dishes:
         if(items[4]==True):
            vegetarian=[]
            print(items[1],"is vegetarian")
            vegetarian.append(items)
            print(vegetarian)

###########################################################################
def print_dishes_ordered_by_price():
    """
        print_dishes_ordered_by_price() function will sort the menu in the order of price (cheap to expensive).
        
        people who want to save money might want the menu printed in order of price, from cheapest to most expensive. you will have to sort the dishes by bubble sort.
        1)first make a copy of the list dishes to sort. do not sort the original list.
        2)code a bubble sort algorithm
        3)print the dishes in the format you used in the first two functions
        
    """
    sorted_dishes = dishes.copy()
    # loop through each element of array
    for item in range(len(sorted_dishes)):

        # keep track of swapping
        swapped = False

        # loop to compare array elements
        for j in range(0, len(sorted_dishes) - item - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if sorted_dishes[j][2] > sorted_dishes[j + 1][2]:
                # swapping occurs if elements
                sorted_dishes[j], sorted_dishes[j + 1] = sorted_dishes[j + 1], sorted_dishes[j]

                swapped = True
        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break
    return sorted_dishes



#########################################################################
def add_dish():
    """
        add_dish() function adds an additional dish to the menu.
        
        In this function you will add a new dish to the menu. 
        You will need many input() statements to get the dish’s name, price, origin, whether it is vegetarian. 
        Then use the inputs to create a tuple for the new dish, and insert the tuple into the list dishes. Last, call the print_menu() function to see your new menu. 
        
        ** Tips: convert the inputs into the right format
        The tuple is (Number, Name, Price, Origin, Whether is vegetarian). 
        What is the number for the new dish? Can you use the len() function?

    """
    
    name = str(input("Enter the new dish's name: "))
    price = int(input("Enter the new dish's price: "))
    origin = str(input("What is the origin of the new dish? "))
    veg = input("Is it vegetarian? True or False? ").lower().strip()
    
    # To convert the entered value into boolean value 
    if veg == 'true':
        vegetarian = True
    elif veg == 'false':
        vegetarian = False
    else:
        print("The entered value is not correct. Please enter True or False.")

    number = len(dishes) + 1

    dishes.append((number, name, price, origin, vegetarian))

    return dishes



############################################################
def apply_discount(price,percentage):
    """
        apply_discount() function takes two arguments, total price and percentage, and returns final price
        
        Use a lambda function to apply the discount percentage. 
        If the price is 100 and discount is 0.2, the discounted price should be 100*(1-0.2)=80. 
        Return the discounted price.

    """
    d=lambda a,b:a-((a*b))/100
 
    return float(d(price,percentage))

 ###############################################################  


def get_order():
    """
        get_order() function takes customer's order and does the following
        
        1. print('Type the number of the dish you want to order and enter. If you are done, type 0 and enter.') 
            The user will input dishes one by one, by entering the number of the dish.
        2. Use a while loop to collect the dishes and put them in a list. The while loop should end if the user enters 0. 
            **Tips: convert the input numbers into integers
        3. Add up the prices of all the dishes. Use a for loop to iterate through the list of dishes the user ordered. 
        4. Print all the dishes the user ordered.
        5. Return the list of dishes the user ordered.
        6. Return the final price 

    """
    #--Complete the function here--
    order=[]
    Custom_order=[]
    dl=len(dishes)
    price=0
    while 2:
        orderlist= int(input("Enter number of dishes you want to order. If you are finished press 0. "))
        if orderlist == 0:
            order.append(orderlist)
            for i in range(0,dl):
                for j in range(0,len(order)):
                    if order[j] == dishes[i][-5]:
                        Custom_order.append(dishes[i])
                        price= price+dishes[i][-3]
            break
        else:
            order.append(orderlist)
    return Custom_order,price




# The menu and main function have been written for you this time. Look over the code and try to understand it. 
# You will be writing your own menu and main function soon.
def menu():
    print('Welcome to Python Kitchen. How may I help you? Enter the number of the option you want to do.')
    print('1.See menu')
    print('2.Order')
    print('3.See dishes in order of price')
    print('4.I am the chef, I want to add a dish to the menu.')
    print('5.Exit')
    

# Main Function: This function calls the functions above. The main function is like the manager of the train station.
# It determines which functions are called, in what order, how many times. It often has additional code as well.
# You may change this code as you please to test your code but the current code will be used to grade your code.

def main():
    c=0
    while(c!=5):
        menu()
        c=int(input())
        if c is 1:
            a=input('Are you vegatarian? Enter Y or N.')
            if (a=='y' or a=='Y'):
                print_vegetarian_menu()
            else:
                print_menu()
        if c is 2:
            order, sum=get_order()
            print('You ordered: ', order)
            print('Your total is ',sum)
            b=input('What is your discount percentage?')
            sum=apply_discount(sum,float(b))
            print('After discount your total is ',sum)
        if c is 3:
            print_dishes_ordered_by_price()
        if c is 4:
            add_dish()
            print('Your new menu is: ')
            print_menu()

    print('Have a good day!')

    pass

#Execute main
main()
# ## IMPORTANT INFORMATION FOR SUBMISSION ###
# Under Homework 3 on Google Classroom, please submit the following
# 1. This file with your name in line 1 (commented) and with your code [.py file]
# 2. For grading: we will use the scenario presented in main to grade so make sure your main method works. 

