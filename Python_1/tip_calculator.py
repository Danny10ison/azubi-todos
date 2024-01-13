"""A program that calculates the total amount
of a meal purchased with a fixed tip.

The program should ask the user to enter the charge for the food.

It should then calculate the amounts of an 18 percent tip and 
7 percent sales tax on the charge of the food and display each of these amounts.

Finally, it should add everything together and display the charge of the 
food plus tip and sales tax.
"""

# ask for user input to enter charge for food
food_charge = float(input("Charge for food = $"))

# calculate 18% tip
tip = food_charge * .18

# calculate 7% sales tax
sales_tax = food_charge * .07

# on the charge of the food and display each of these amounts
print("Tip = ${:.2f}".format(tip))
print("Sales tax = ${:.2f}".format(sales_tax))
print("Grand total = ${:.2f}".format(food_charge + tip + sales_tax))
