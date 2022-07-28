# Create a program that can calculate total cost of 
# all the items in shopping cart given prices = [10, 20, 30]

prices = [10, 20, 30]
total_price = 0
for cost in range(0, len(prices)):
 total_price += prices[cost]
print(total_price)