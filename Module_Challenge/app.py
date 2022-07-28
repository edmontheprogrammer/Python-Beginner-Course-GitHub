# Write a program that imports a module called 'utils' 
# and uses a function from 'utils' called find_max() that 
# returns the largest number from a list

from utils import find_max

numbers = [10, 3, 6, 2]
max_number = find_max(numbers)
print(max_number)