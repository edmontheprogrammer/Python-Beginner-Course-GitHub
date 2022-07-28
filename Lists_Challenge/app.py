# Write a program to find the largest number in a list
# create a numbers list
# find the largest number using math method. 

# numbers = [4, 19, 2, 107, 0, 61]
# max_number = max(numbers)
# print(max_number)

numbers = [3, 6, 2, 10, 8, 4]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)