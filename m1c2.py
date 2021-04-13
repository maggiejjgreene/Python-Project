# Create and print list names
names = ['Apple Inc','Coca-Cola', 'Walmart']
print(names)

# Create and print list prices
prices = [159.54, 37.13, 71.17]
print(prices)

# Print the first item in names
print(names[0])

# Print the second item in names
print(names[1])

# Print the last element in prices
print(prices[-1])

# names
names = ['Apple Inc', 'Coca-Cola', 'Walmart']

# Use slicing on list names
names_subset = ['Coca-Cola','Walmart']
print(names_subset)

# Create and print the nested list stocks
stocks = [names, prices]
print(stocks)

# Use list indexing to obtain the list of prices
print(stocks[1])


# Use indexing to obtain company name Coca-Cola
print(stocks[0][1])

# Use indexing to obtain 71.17
print(stocks[1][2])

# Print the sorted list prices
prices = [159.54, 37.13, 71.17]
prices.sort()
print(prices)

# Append a name to the list names
names.append('Amazon.com')
print(names)

# Extend list names
more_elements = ['DowDuPont', 'Alphabet Inc']
names.extend(more_elements)
print(names)

# Do not modify this
max_price = max(prices)

# Identify index of max price
max_index = prices.index(max_price)

# Identify the name of the company with max price
max_stock_name = names[max_index]

# Fill in the blanks
print('The largest stock price is associated with ' + max_stock_name + ' and is $' + str(max_price) + '.')