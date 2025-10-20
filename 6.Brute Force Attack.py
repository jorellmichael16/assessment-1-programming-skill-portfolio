# -*- coding: utf-8 -*-
"""
Created on Sun Oct 12 23:18:36 2025

@author: jorel
"""
password = (input("Make a password "))#asks the user for a password
attempts = 0
while attempts <= 6: #loops six times
    pasword = (input("Enter your password "))
    if pasword == password: #checks if the pasword attempted is the same as the made password
      print("Your password is correct, Welcome!")
      break # stops the loop if the pasword is correct
    elif attempts == 5: # stops the loop if it reaches max attempt
        print("You have maxed out your attempts")
        break;
  
    else: #begins the loop
       print("Your password is Incorrect, try again")
       attempts += 1
       print("Attempts made", attempts, ", you have 5 attempts" )
       
      
      

      