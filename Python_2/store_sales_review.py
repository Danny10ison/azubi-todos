"""Store sales review project

Azubi store has products that customers love. Below are the products, prices and the number of customers that purchased products last week.

The owner wants you to do some calculations on the data with these criteria's:

    -calculate the total price average for all products

    -create a new price list that reduces the old prices by $ 5

    -calculate the total revenue generated from the products

    -calculate the average daily revenue generated from the products

    -based on the new prices, which products are less than $ 30 
"""

products = ["Sankofa Foods", "Jamestown Coffee",
            "Bioko Chocolate", "Blue Skies Ice Cream",
            "Fair Afric Chocolate", "Kawa Moka Coffee",
            "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]


print("Original price:", prices)
print()

# calculate the total price average for all products
# total_price_average = sum(all prices) / the number of items
print("Total price average: {:.2f}".format(sum(prices) / len(prices)))

# create a new price list that reduces the old prices by $ 5

new_prices = []
for price in prices:
    new_prices.append(price - 5)
print("Prices reduced by 5:", new_prices)

# calculate the total revenue generated from the products
total_revenue = 0
for i in range(len(prices)):
    total_revenue += prices[i] * last_week[i]
print("Total revenue:{:.2f}".format(total_revenue))

# calculate the average daily revenue generated from the products
average_daily = total_revenue / sum(last_week)
print("Average daily:{:.2f}".format(average_daily))

# based on the new prices, which products are less than $ 30
prod_less_30 = []

for prod, price in zip(products, prices):
    if price < 30:
        prod_less_30.append(prod)
print("Prods less 30:", prod_less_30)
