# if name is less than 3 characters long 
#   name must be at least 3 characters 
# otherwise it it's more than 50 characters long name can be a maximum 
#                 of 50 characters 
# otherwise
#   name looks good 

# Psudocodes:
# Create a variable 'name' and assign it to input('Enter your name ')
# Convert 'name to integer'
# create if-elif-else statment that compares if name <3; else if > 50
# else name can be a maxium of 50 characters

name = input('Enter your name ')
name_length = len(name)
print(name_length)
if name_length < 3:
    print('name must be at least 3 characters')
elif name_length > 50:
    print('name can be a maxium of 50 characters')
else:
    print('name looks good!')
