# Katia Hourany

### English Words Workshop ###

# Make sure to download the english_dictionary.txt file from Google Classroom (under Homework 4)
# You will need the file path to open/close file in this code.
# PLEASE READ COMMENTS TO HELP YOU WRITE THE CODE AND ASK QUESTIONS IN PIAZZA OR GOOGLE CLASSROOM

# For submission:
# 1. Replace the first line with your name (in comment)
# 2. Write methods convert_file_to_dict, get_definition, get_pos
# 3. Test your code using test_get_definition and test_get_pos
# 4. Submit this hw4.py file to Google Classroom under Homework 4.

def convert_file_to_dict():
    """
    
        convert_file_to_dict opens english_dictionary.txt and creates a dictionary where
        words are the keys and the value is a list of pos, meaning(s).
        
        TODO: Read comments and figure out how to create a dictionary based on a txt file.
        You will need to know how to access a file and parse through each line and create a 
        dictionary. You will also need to apply text pre-processing methods discussed in lecture 4.
        
    """


    
    # 1. For each line, split it into the word, its part of speech(POS), and its meanings
    #    HINT: The word and the POS is separated by ‘(‘. The POS and meanings are separated by ‘)’.
    #          The different meanings are separated by ‘;’.  
    #          Remove the extra whitespace around the word and the POS. 
    # 2. Insert the word into a new data structure. 
    #    HINT: You should create this data structure before the for loop. 
    #          It is a dictionary, and the keys are the words. 
    #          Each word has a list in this format: [pos, [meaning1, meaning2,...]].  
    
    dictionary = {}
    lines=[line.strip() for line in open("C:/Users/User/Desktop/PYTHON/lecture 4/english_dictionary.txt")]
    # print(lines)
    dictionary = {}

    for element in lines:
        if element:
            word, Pos = element.split("(", 1)
            Pos, definition = Pos.split(")", 1)
            # word = word.strip()
            Pos = Pos.strip()
            definition = definition.split(";")
            
            # print(word)
            # print(Pos)
            # print(definition)
            if word not in dictionary:
                dictionary[word] = []
            dictionary[word].append([Pos, definition])

    print(dictionary)
    return dictionary

def get_definition(dictionary, word):
    """
    
        get_definition() will return the defintion of the word in string format
        
        dictionary: dict containing all the words and their pos + definitions
        
        TODO: Figure out how to access the definition(s) of each word and how to 
        handle multiple definitions.
        
        You should return string that looks like this
        '[word] means [definition]'
        or if there are multiple definitions:
        '[word] means [definition1], [definition2],...
        
        Example: Accuser means one who accuses, one who accuses, one who brings a charge of crime or fault.
        
        HINT: Take note of definition casing (lowercase/uppercase) and make sure to remove whitespace and \n characters
        using the builtin strip() method.
        
    """
    definition = []
    L=len(list(dictionary[word]))
    for i in range(1,L):  
        definition += list(dictionary[word][i][1])
        
    print(definition)
    return definition
        
def get_pos(dictionary, word):
    """
        get_pos will return the pos in string format
        
        TODO: Figure out how to access the pos in the dictionary.
        
        You should return string that looks like this
        '[pos]'
              
        Example: n.
        
        HINT: Make sure to remove whitespace and \n characters using the builtin strip() method.
        
    """
    pos = ""
    L=len(list(dictionary[word]))
    for i in range(1,L):  
         pos += list(dictionary[word][i][0])
         
    print(pos)
        
    return pos

def main():
    # feel free to modify main method as needed for testing purposes.
    dict_1 = convert_file_to_dict()
    print(get_definition(dict_1, 'Acetimeter '))
    print(get_definition(dict_1, 'Accuser '))
    
    # print(get_pos(dict_1, 'Accuser '))
    # print(get_pos(dict_1, 'Abstracting '))
    
    
### TEST METHODS (will be used for grading!) ###
    
def test_get_definition():
    dict_1 = convert_file_to_dict()
    result_1 = get_definition(dict_1, 'Accuser ')
    expected_1 = "Accuser means one who accuses, one who accuses, one who brings a charge of crime or fault."
    
    # assert expected_1 == result_1.strip()
    
    result_2 = get_definition(dict_1, 'Acetimeter ')
    expected_2 = "Acetimeter means an instrument for estimating the amount of acetic acid in vinegar or in any liquid containing acetic acid."
    
    # assert expected_2 == result_2.strip()

# def test_get_pos():
#     dict_1 = convert_file_to_dict()
#     result_1 = get_pos(dict_1, 'Accuser')
#     expected_1 = "n."
    
#     assert expected_1 == result_1.strip()
    
#     result_2 = get_pos(dict_1, 'Abstracting')
#     expected_2 = "p. pr. & vb. n."
    
#     assert expected_2 == result_2.strip()  
    
if __name__ == "__main__":
    main()
    test_get_definition()
    # test_get_pos()
