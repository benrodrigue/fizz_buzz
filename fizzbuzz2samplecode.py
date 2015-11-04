#!/usr/bin/env python 3


# Quality solution found online 

for num in range(1,101):
    msg = ''
    if num % 3 == 0:
        msg += 'Fizz'
    if num % 5 == 0:       
        msg += 'Buzz'
    print(msg or num)
   
# Old code
   
    if eval_num % 3 == 0 and eval_num % 5 == 0:
        print("fizzbuzz")
    elif eval_num % 3 == 0:
        print("fizz")
    elif eval_num % 5 == 0:
            print("buzz")
    else:
        print(eval_num)
        
    eval_num += 1