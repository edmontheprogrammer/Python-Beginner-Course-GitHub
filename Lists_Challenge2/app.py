# Write a program to remove the duplicates in a list

mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

# Example Explained

# Frist we have a list that contains duplicates
# mylist = ["a", "b", "a", "c", "c"]

# Create a dictionary, using the list items as keys. 
# This will automatically remove any duplicates because 
# dictionaries cannot have duplicate keys

# Create a Dictionary
# mylist = mylist(dict.fromkeys(mylist))
# print(mylist)


