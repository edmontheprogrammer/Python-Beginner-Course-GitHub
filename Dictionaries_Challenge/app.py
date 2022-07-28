# Write a program that allows the user to type integers 
# and outputs the integers in words such as 
# Phone: 1, 2, 3, 4
# One Two Three Four 

phone = input("Phone: ")
digit_mapping = {"0": "Zero", "1": "One", "2": "Two", "3": "Three", "4": "Four", 5: " Five",
 "6": "Six", "7": "Seven", "8": "Eight", "9": "Nine"}
output = ""
for ch in phone: 
    output += digit_mapping.get(ch, "!") + " "
print(output)