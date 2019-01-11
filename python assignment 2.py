# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 12:50:02 2019

@author: thanusha
"""

#problem statement 1
#comma separated numbers from console to generate a list

data =input("enter the data:") #input from console
listcreated =data.split(',')   #split the input by comma
print(listcreated) # printing the list

#problem statement 2
# creating star pattern

n=5 # taking n as 5
#using nested for loop to print star pattern
for i in range(n):      # outer for loop for row count   
    for j in range(i):  # inner for loop for column count
        print ('* ', end="")
    print('')

for i in range(n,0,-1): # for loop to iterate in decending order
    for j in range(i):
        print('* ', end="")
    print('')
    
#problem statement 3
#  reverse of word

Enter_name = input("enter a word to reverse : ") #taking input from console using input
Entered_word= Enter_name[::-1]                   #reverse the enter word by using index from last element
print("reverse of entered word :", Entered_word) #printing the required output

#problem statement 4

print('WE, THE PEOPLE OF INDIA,\n\t having solemnly resolved to constitute India into a SOVEREIGN, ! \n\t \t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t ' ' and to secure to all its citizens')  
# \n new line character
# \t new tab
# ' ' create a space i.e space character
