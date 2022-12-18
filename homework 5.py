# Katia Hourani

# ## Homework 5: Practice Recursion ###

# PLEASE READ COMMENTS TO HELP YOU WRITE THE CODE AND ASK QUESTIONS IN PIAZZA OR GOOGLE CLASSROOM

# For submission:
# 1. Replace the first line with your name (in comment)
# 2. Write methods palindrome, sum_even, quicksort
# 3. Test your code using test_palindrome, test_sum_even, test_quicksort
# 4. Submit this hw5.py file to Google Classroom under Homework 5.

# 1.Write a recursive function to determine in a word 
# is a palindrome (the word is the same read backwards, 
# like “wow”, “mom”, “malayalam”) .
def palindrome(word):
    """ 
        palindrome: takes in 'word' and returns True if 'word' is palindrome or 
        False if 'word' is not a palindrome.
    """


    if len(word) < 1:
        
        return True
    else:
        if word[0] == word[-1]:
            return palindrome(word[1:-1])
        else:
      
            return False


     
# 2. Write a recursive function to calculate the sum 
# of even numbers from 1 to n. (if n is 9, you should 
# sum 2+4+6+8. If n is 12, you should sum 2+4+6+8+10+12)
# You can assume num will always be positive.
def sum_even(num):
    """
        sum_even: takes in 'num' and returns sum of even numbers from 1 to n.
    """
    
    if num<=0:
        return 0
    if not num % 2 == 0:
        return sum_even(num-1)
    else:
        return num + sum_even(num-2)
  

# 3. Implement quicksort with recursion to sort a list.
# Here is a list that you can use:
# array = [10, 3, 1, 4, 6, 8]
def quicksort(array):
    """
        quicksort: takes in 'array' and returns sorted array.
    """
    elements = len(array)
    
    #Base case
    if elements < 2:
        return array
    
    current_position = 0 #Position of the partitioning element

    for i in range(1, elements): #Partitioning loop
         if array[i] <= array[0]:
              current_position += 1
              temp = array[i]
              array[i] = array[current_position]
              array[current_position] = temp

    temp = array[0]
    array[0] = array[current_position] 
    array[current_position] = temp #Brings pivot to it's appropriate position
    
    left =  quicksort(array[0:current_position]) #Sorts the elements to the left of pivot
    right = quicksort(array[current_position+1:elements]) #sorts the elements to the right of pivot

    array = left + [array[current_position]] + right #Merging everything together
    
    return array

 

def main():
    print(palindrome('malayalam'))
    print(palindrome('hello'))
    
    print(sum_even(9))
    print(sum_even(123))
    
    print(quicksort([10, 3, 1, 4, 6, 8]))
    

### TEST METHODS (will be used for grading!) ###
def test_palindrome():
    assert palindrome('malayalam')
    assert palindrome('racecar')
    assert not palindrome('hello')
    assert not palindrome('world')

def test_even_sum():
    assert sum_even(9) == 20
    assert sum_even(20) == 110
    assert sum_even(123) == 3782
    
def test_quicksort():
    assert quicksort([10, 3, 1, 4, 6, 8]) == [1, 3, 4, 8, 8, 10]
    assert quicksort([65, 2, 12, 1]) == [1, 2, 12, 65]
    
if __name__ == "__main__":
    main()
    test_palindrome()
    test_even_sum()
    test_quicksort()
    
