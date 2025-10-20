# -*- coding: utf-8 -*-
"""
Days of the month
"""
Month = {
        1: "January",
        2: "Febuary",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
        } #assigns 1-12 into a string
Days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
        } #assigns 1-12 into numbers
a = int(input("What month you wanna know twin? "))#asks the user for a number
if a in Days:#checks if the number inputed is in days
    print("Your Month is", Month[a], "and the days are", Days[a])
#prints the month and days you wanted to now
else:
    print("Your number is not in the list gng")
#if the number inputed is not in the list, this will pop up