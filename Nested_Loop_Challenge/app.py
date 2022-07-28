# numbers = [5, 2, 5, 2, 2]
# Using the numbers array above print the following shape
# using an inneer-loop. Dot multiply number * 'X' such as 5 * 'X'
# XXXXX
# XX 
# XXXXX
# XX 
# XX 

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
