#!/usr/bin/env python 3

# Count from 1 to 100
# On numbers divisible by 3 change to fizz and 5 change to buzz; 3 and 5 fizzbuzz

import sys

if len(sys.argv) > 1:
    max_num = int(sys.argv[1])
    print(max_num)
elif len(sys.argv) <= 1:
    max_num = int(input("Fizzbuzz is a game that will replace numbers divisible by 3 and 5 with the words fizz and buzz. How high should we count today?  "))
    print(max_num)

for num in range(1,max_num):
    msg = ""
    if num % 3 == 0:
       msg += "Fizz"
    if num % 5 == 0:
       msg += "Buzz"
    print(msg or num)
        

    
