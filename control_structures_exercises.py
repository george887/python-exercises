#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1.A. prompt the user for a day of the week, print out whether the day is Monday or not

is_today_monday = True

if is_today_monday:
    print("Today is Monday :(")
else:
    print("Today is not Monday!")


# In[ ]:


# 1. B. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day = "Monday"
if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print(f'{day} is on a weekday')
else:
    if day == "Saturday" or day == "Sunday":
        print(f'{day} is on a weekend')


# In[8]:


day = input("Please enter a day of the week ")

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print(f'You entered {day} and its a weekday')
else:
    if day == "Saturday" or day == "Sunday":
        print(f'{day} is on a weekend')


# In[17]:


#1 C. create variables and make up values for 
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

hrs_worked_in_week = 45
hourly_rate = 28
extra_hrs_worked = 5
over_time_rate = 28 * 1.5
paycheck = hrs_worked_in_week * hourly_rate
o_paycheck = (40 * 28) + extra_hrs_worked * over_time_rate

if hrs_worked_in_week <= 40:
    print(paycheck)
elif hrs_worked_in_week > 40:
    print(o_paycheck)
    


# In[30]:


# 2.A 'While' Create an integer variable i with a value of 5. Create a while loop that runs so long as i
# is less than or equal to 15 Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i = i +1


# In[29]:


## Answered with for
for i in range(1,16):
    print(i)


# In[37]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a 
# new line.
i = 0
while i <= 100:
    print(i)
    i = i + 2


# In[33]:


## Answered with for
for i in range(0, 101, 2):
    print(i)


# In[34]:


# Alter your loop to count backwards by 5's from 100 to -10.
i = 100
while i >= -10:
    print(i)
    i = i - 5


# In[35]:


## Answered with for
for i in reversed(range(-10, 105, 5)):
    print(i)


# In[34]:


# Create a while loop that starts at 2, and displays the number squared on each line while the number is 
# less than 1,000,000. Output should equal:
i = 2
while i < 1000000:
    print(i)
    i = i ** 2
    


# In[35]:


# Write a loop that uses print to create the output shown below.
i = 100
while i > 0:
    print(i)
    i = i - 5


# In[70]:


#2.B. For Loops. Write some code that prompts the user for a number, then shows a multiplication table up 
# through 10 for that number. 
number = int(input("Please enter a number:"))
for i in range(1,11):
    print(number, "X", i, "=", number * i)


# In[78]:


# Create a for loop that uses print to create the output shown below.
for i in range(1,10):
    print(str(i) * i)
for i in range(1,10):
    print(str('cat') * i)


# In[29]:


# break and continue Prompt the user for an odd number between 1 and 50. Use a loop and a break statement
# to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings 
# to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.

number = (input("Please enter an odd number between 1 & 50:"))
for i in range(1,51,2):
    while number.isdigit() == False or int(number) % 2 == 0 or int(number) < 1 or int(number) > 50:
        print(f"You pick an invalid number {number}. Please pick an odd number between 1 & 50.")
        number = (input("Please enter an odd number between 1 & 50:"))
        if number.isdigit() == True or int(number) % 2 == 1 and int(number) >= 1 and int(number) < 50:
            print("\n", number, "is the number to skip\n")
            break
    if i == int(number):
        print(f"Yikes! Skipping {i}:",i)
        continue
    print("Here is an odd number", i)


# # 

# 

# In[30]:


# The input function can be used to prompt for input and use that input in your python code. Prompt the user 
# to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that 
# the value the user entered is a valid number, also note that the input function returns a string, so you'll
# need to convert this to a numeric type.)
number = (input("Please enter an even number between 0 & 70:"))
for i in range(0,71,2):
    while number.isdigit() == False or int(number) % 2 == 1 or int(number) < 0 or int(number) > 70:
        print(f"You pick an invalid number {number}. Please pick an even number between 1 & 70.")
        number = (input("Please enter an even number between 1 & 70:"))
        if number.isdigit() == True or int(number) % 2 == 0 and int(number) >= 0 and int(number) < 71:
            print("\n", number, "is the number to skip\n")
            break
    if i == int(number):
        print(f"Yikes! Skipping {i}:",i)
        continue
    print("Here is an even number", i)


# In[38]:


# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers
# from the number the user entered down to 1.
number = (input("Please enter an even number between 0 & 20:\t"))
for i in reversed(range(0,21,2)):
    while number.isdigit() == False or int(number) % 2 == 1 or int(number) < 0 or int(number) > 20:
        print(f"You pick an invalid number {number}. Please pick an even number between 1 & 20.")
        number = (input("Please enter an even number between 1 & 20:"))
        if number.isdigit() == True or int(number) % 2 == 0 and int(number) >= 0 and int(number) < 21:
            print(number, "is the number to skip")
            break
    if i == int(number):
        print(f"Yikes! Skipping {i}:",i)
        continue
    print("Here is an even number", i)


# In[45]:


3. # Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
3

for Fizzbuzz in range(1,101,1):
    if Fizzbuzz % 3 == 0 and Fizzbuzz % 5 == 0:
        print("Fizzbuzz")
        continue
    elif Fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    elif Fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    print("Here is a number", Fizzbuzz)
    
    


# In[75]:


# Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
running = True

while running:
    number = int(input("What number would you like to go up to?:\t"))
   
    for x in range(1, number + 1):
        print(x, x ** 2, x **3)

    question = input("Would you like to do another table? Yes or No?:\t")
    if question == "No":
        break
    else:
        continue
    
                
            
        


# In[95]:


# 5 Convert given number grades into letter grades. 
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:

# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

running = True

while running:
    grade = int(input("Please enter your numerical grade "))
    if grade <= 100 and grade >= 88:
        print(f"You received an A with a {grade}")
    elif grade <= 87 and grade >= 80:
        print(f"You received an B with a {grade}")
    elif grade <= 79 and grade >= 67:
        print(f"You received an C with a {grade}")
    elif grade <= 66 and grade >= 60:
        print(f"You received an D with a {grade}")
    elif grade <= 59:
        print(f"You received an D with a {grade}")
    question = input("Would you like to input another grade? Yes or No?:\t")
    if question == "No":
        break
    else:
        continue
        
                


# In[122]:


# Create a list of dictionaries where each dictionary represents a book that you have 
# read. Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the
# titles of all the books in that genre.
Books = [
    {"Title": "Childrens Everyday Bible",
          "Author": "Deborah Chancellor",
          "Genre": "Biblical"
         }, 
        {
            "Title": "Mr. Brown can Moo! Can You?",
          "Author": "Dr. Seuss",
          "Genre": "Childrens Fiction"
        },
        {
            "Title": "Start With Why",
          "Author": "Simon Sinek",
          "Genre": "Self Help Book"
        }]
for Title in Books:
    print(Title)

prompt = input("Enter a genre ")
while prompt not in [x['Genre'] for x in Books]:
    prompt = input('Please enter a new genre as the specified one is not in this dictionary: ')
    if prompt in [x['Genre'] for x in Books]:
        break
for x in Books:
    if prompt == x['Genre']:
        print("{} Falls under the genre of {}".format(x['Title'], prompt))


# In[ ]:





# In[ ]:




