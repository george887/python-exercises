#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Define a function named is_two. It should accept one input and return True if the assed input is either 
# the number or the string 2, False otherwise.

# defining the function is_two with a single variable x as a string
def is_two(x):
    # allowing the variable to be both an interger and string when equal to two
    if int(x) == 2 or str(x) == 2:
        # returning a true bool if true
        return True
    # otherwise return the false bool
    else:
        return False

assert type(is_two(2)) == bool
is_two(2)


# In[2]:


#2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# defining is_vowel with a single variable x as a string
def is_vowel(x):
    # if the variable x is either a lower or upper case vowel
    if x in ["a", "e", "i", "o", "u"] or x in ["A", "E", "I", "O", "U"]:
        # return a true bool
        return True
    # otherwise false
    else:
        return False
    
assert type(is_vowel("D")) == bool
is_vowel("D")  


# In[3]:


is_vowel("A")


# In[4]:


#3. Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

# defining is_consonant function with a single string as a varible
def is_consonant(x):
    # refering to is_vowel function to see if the sting is a vowel
    if is_vowel(x):
        # returning the bool False if vowel
        return False
    # otherwise returning true for being a consonant
    else:
        return True

is_consonant("O")


# In[5]:


is_consonant("C")


# In[6]:


#4. Define a function that accepts a string that is a word. The function should capitalize the first letter
# of the word if the word starts with a consonant.

# defining a the cap_first_letter_word function with a string value
def cap_first_letter_word(word):
    # refering to the is_consonant function to see if the string first letter is a consonant
    if is_consonant(word[0]):
        # returning the first letter uppercased with the remainder of the word unchanged
        return (word[0].upper() + word[1:])
    # otherwise returning the word unchanged
    else:
        return word
    


# In[7]:


cap_first_letter_word("ant")
cap_first_letter_word("dog")


# In[8]:


#5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and
# the bill total, and return the amount to tip.

#defining the function calculate tip with two variables which will return a float since we are dealing with decimals. It could return an int if we give no tip or give an 100% tip
def calculate_tip(tip_percentage, bill_total):
    # assigning a new variable to accept the two variables above
    tip_amount = bill_total * tip_percentage
    #returning the tip_ampout
    return tip_amount
    
    


# In[9]:


calculate_tip(.15,50)


# In[10]:


#6. Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.

# defining the apply_discount function with two variables
def apply_discount(original_price, discount_percentage):
    # assigning a new variable that takes in the two variables listed above. 
    price_after_discount = original_price - (original_price * discount_percentage)
    # returning the price_after_discount as an float or int since dealing with numbers
    return price_after_discount


# In[11]:


apply_discount(55, .3)


# In[12]:


#7. Define a function named handle_commas. It should accept a string that is a number that contains commas
# in it as input, and return a number as output.

# defining the function with a string
def handle_commas(number):
    #creating a variable remove_commas to take the number we give and replace "," with a space
    remove_commas = number.replace(",","")
    return remove_commas


# In[13]:


handle_commas("4,4,44,")


# In[14]:


#8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated
# with that number (A-F).

# defining a function with a string
def get_letter_grade(grade):
        # setting parameters for grade to fall in and produce the corresponding letter grade
        if grade >= "90" and grade < "100":
            return "A"
        elif grade <= "89" and grade >= "80":
            return "B"
        elif grade <= "79" and grade >= "70":
            return "C"
        elif grade <= "69" and grade >= "60":
            return "D"
        else:
            return "F"


# In[15]:


get_letter_grade("60")


# In[16]:


#9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels
# removed.

#defining a function with a string
def remove_vowels(word):
    #creating a variable to show all possible vowels
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    # creating a for loop to look at the characters in the word
    for char in word:
        # asking if any characters in the word are vowels
        if char in vowels:
            #removing the vowel if present
            word = word.replace(char, "")
            return word


# In[17]:


remove_vowels("dog")


# In[18]:


#10. Define a function named normalize_name. It should accept a string and return a valid python identifier, 
# that is: anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

def normalize_name(word):
    removing_not_valid_py_id = (word.strip("0123456789").lower().replace(" ", "_"))
    remove_special_char = ""
    for x in removing_not_valid_py_id:
        if x not in "!@#$%^&*()+=-[]{}\/|?.<>,`~":
            remove_special_char += x
    return remove_special_char


# In[19]:


normalize_name("23  ssDDWd() ?}")


# In[20]:


#11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the 
# cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(numbers):
    list = []
    length = len(list)
    list = [sum(numbers[0:x + 1]) for x in range(len(numbers))]
    return list[1:] 

cumulative_sum([10,20,30,40,50])


# In[21]:


# Bonus Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and 
# return a string that is the representation of the time in a 24-hour format. Bonus write a function that 
# does the opposite.
def twelveto24(time):
    # Checking if last two elements of time 
    # is AM and first two elements are 12 
    if time[-2:] == "AM" and time[:2] == "12": 
        return "00" + time[2:-2] 
          
    # remove the AM     
    elif time[-2:] == "AM": 
        return time[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif time[-2:] == "PM" and time[:2] == "12": 
        return time[:-2] 
          
    else: 
        # add 12 to hours and remove PM 
        return str(int(time[:2]) + 12) + time[2:8] 

twelveto24("3:14AM")


# In[ ]:





# In[ ]:




