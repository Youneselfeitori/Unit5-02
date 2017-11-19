# Created by: Younes Elfeitori
# Created on: Nov 2017
# Created for: ICS3U
# This program selects 10 numbers from 1 to 10 and selects the biigest value

from numpy import random

def find_max_value(array):
    # finds largest number
    max_value = max(array)
   
    return max_value 

# input
counter = 0
random_numbers = []

while counter < 10:
    single_number = random.randint(1, 10 + 1)
    print(single_number)
    random_numbers.append(single_number)
    counter = counter + 1

# process
largest_value = find_max_value(random_numbers)

# output
print("\nThe largest number is: " + str(largest_value))
