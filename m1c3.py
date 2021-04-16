# Import numpy as np
import numpy as np

# Lists
prices = [170.12, 93.29, 55.28, 145.30, 171.81, 59.50, 100.50]
earnings = [9.2, 5.31, 2.41, 5.91, 15.42, 2.51, 6.79]

# NumPy arrays
prices_array = np.array(prices)
earnings_array = np.array(earnings)

# Print the arrays
print(prices_array)
print(earnings_array)

# Create PE ratio array
pe_array = np.array(prices)/np.array(earnings)

# Print pe_array
print(pe_array)

# Subset the first three elements
prices_subset_1 = prices_array[0:3]
print(prices_subset_1)

# Create a 2D array of prices and earnings
stock_array = np.array([prices, earnings])
print(stock_array)

# Print the shape of stock_array
print(stock_array.shape)

# Print the size of stock_array
print(stock_array.size)

# Transpose stock_array
stock_array_transposed = np.transpose(stock_array)
print(stock_array_transposed)

# Print the shape of stock_array
print(stock_array_transposed.shape)

# Print the size of stock_array
print(stock_array_transposed.size)

# Subset prices from stock_array_transposed
prices = stock_array_transposed[:, 0]
print(prices)

# Subset earnings from stock_array_transposed
earnings = stock_array_transposed[:, 1]
print(earnings)
# Subset the price and earning for first company
company_1 = stock_array_transposed[0, :]
print(company_1)
# Calculate the mean
prices_mean = np.mean(prices)
print(prices_mean)

# Calculate the standard deviation
prices_std = np.std(prices)
print(prices_std)


# Create and print company IDs
company_ids = np.arange(1, 8, 1)
print(company_ids)

# Use array slicing to select specific company IDs
company_ids_odd = np.arange(1, 8, 2)
print(company_ids_odd)

# Find the mean
price_mean = np.mean(prices)

# Create boolean array
boolean_array = (prices > price_mean)
print(boolean_array)

# Select prices that are greater than average
above_avg = prices[boolean_array]
print(above_avg)

sectors = np.array("Health_care")
# Create boolean array

boolean_array = (sectors == 'Health Care')
print(boolean_array)

names = np.array("health_care")

# Print only health care companies
health_care = names[boolean_array]
print(health_care)

