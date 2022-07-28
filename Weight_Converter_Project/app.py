# Create a weight convertor program that allows the user to 
# enter their weight either in lbs or kg and converts it into 
# the other weight (lbs or kg) prompting the user 
# prompt the user either they choose pounds or kg as units 
# Add on to the Type Conversions Challenge
# Ask the user to enter their weight and then convert it to the 
# other unit 

weight = int(input('Weight: '))
unit = input('(L)lbs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight // 0.45
    print(f"You are {converted} pounds")
