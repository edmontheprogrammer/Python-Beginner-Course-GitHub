# Create a car game that allows the user to drive the car
# the user should be able to type in the following commands 
# to operate the car.
# start - to start the car
# stop - to stop the car
# quit - to exit 
# If the user type anything other than the commands above 
# do nothing, and print I don't understand that ... 

# Pseudocodes: 
# write a print statment with instructions for the game 
# Create a variable that stores the user input. 
# create a while-loop that loops forever until the user types in 
# quite to exit the loop, terminates
# write if statments that compares user inputs to the expected
# values: 'start', 'stop' 'quit'

print('Welcome to the Car Game input the following commands to play')
print('start - to start the car')
print('stop - to stop the car')
print('quit - to exit')

while True:
    value = input('>')
    if value == "start":
        print('Car started...Ready to go!')
    elif value == "stop":
        print("Car stopped.")
    elif value == "quit":
        break
    else: 
        print("I don't understand that...")
