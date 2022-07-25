# Challenge As a user for their weight (in pounds), convert it to 
# kilograms and print on the terminal 

# Pseudo Codes
# Step 1: write an input() function to ask the user for their weight  
#           in pounds. 
#         Add the question as a parameter inside the input() method
# Step 2: Convert the string value entered by the user into a floating
#           floating value, so you don't lose data
# Step 3  Google the conversion rate from pounds to kilogram and 
#         use math operators for calcuations
# Step 4: Write a print() fuction to output the results   
user_weight_in_pounds = float(input('Enter your weight in pounds '))
kilogram = 0.453592
user_weight_in_kilograms = user_weight_in_pounds * kilogram
print(user_weight_in_kilograms)
