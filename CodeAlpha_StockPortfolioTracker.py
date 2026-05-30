# stock prices dictionary
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 400,
    "AMZN": 175,
    "NVDA": 900
}

print("Available stocks:", list(prices.keys()))

# Lists to save user data
my_stocks = []
my_quantities = []

# Get number of stocks
num_stocks = input("How many different stocks do you own? ")
num_stocks = int(num_stocks)

# to get user inputs
for i in range(num_stocks):
    name = input("Enter stock symbol: ")
    name = name.upper()

    if name in prices:
        shares = input("Enter number of shares: ")
        shares = int(shares)

        my_stocks.append(name)
        my_quantities.append(shares)
    else:
        print("Stock not found. Skipping!")

# Calculate total value
print("\n--- SUMMARY ---")
total_value = 0

for i in range(len(my_stocks)):
    stock = my_stocks[i]
    qty = my_quantities[i]
    price = prices[stock]

    stock_value = qty * price
    total_value = total_value + stock_value

    print(f"{stock}: {qty} shares x ${price} = ${stock_value}")

print("Total Value: $" + str(total_value))

# Save result in a text file
file = open("portfolio.txt", "w")
file.write("Total Value: $" + str(total_value))
file.close()

print("Result saved in portfolio.txt")