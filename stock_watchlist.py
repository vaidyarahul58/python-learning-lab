# Stock Market wachlist having 9 stocks in the list sorted as per their prices.
# another list is having their respective prices.
# sort the Stocks list in assending order.
# Remove low priced 3 stocks from the list.
# Show the high prices at top.

stocks = ["ONGC", "BEL", "SBIN", "JSWSTEEL", "DRREDDY", "ADANIPORTS", "LT", "INDIGO", "EICHERMOT"]
prices = [225.00, 377.20, 973.70, 1241.20, 1242.50, 1766.00, 3661.90, 4700.00, 7349.00]

# Printing original list with their respective prices.
print("======== Watchlist ========")
for i in range(len(stocks)):
    print(stocks[i], prices[i])
print("===========================")

# Preserving original stock list
ostock = stocks

# Sorting stocks list in assending order.
stocks.sort() # Sorting stocks list in assending order
print("====== Sorted Watchlist ======")
print(stocks)
print("==============================")

# Remove low priced 3 stocks from the list. but before remove print check other stocks.
# Printing stocklist other than 3 low priced.
# print(stocks[3:]) # printing stocks list in onel line hence changed the code.
print("\n===== High Value Stocks ======") 
for i in range(3, len(ostock)):
    print(ostock[i], prices[i])
print("================================")

# Removing 3 low priced stocks
del(ostock[:3])
del(prices[:3])
# print("\n- Removing low priced 3 stocks from list")
# print(stocks.remove[:3])
# print(prices.remove[:3])
print(stocks)
print(prices)
# prices sort reverse to show high priced at top.
stocks.sort(reverse=True)  # Sorting list in decending order.
print("\n------Reverse sorted Watchlist------")
for i in range(len(stocks)):
    print(stocks[i]) 
               




    

