# Imagine the price of the house is $1 million
# If the buyer has good credit, 
#   they need to put down 10%
# Otherwise 
#   they need to put down 20% 
# print the down payment

price_of_house = 1000000
good_credit = True
down_payment = 0

if good_credit:
    down_payment = (10/ 100) * price_of_house
    print(down_payment)
else:
    down_payment = (20/100) * price_of_house
    print(down_payment)

