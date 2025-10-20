# -*- coding: utf-8 -*-
"""
Simple Search
"""
names=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
search=input("Enter the name you want to search for: ")
if search in names:
    print(f"{search} was found in the list")
else:
    print(f"{search} was not found in the list")

