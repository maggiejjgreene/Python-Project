import pandas as pd
data = pd.read_csv("stock_data2.csv")
print(data.info())

# Import matplotlib.pyplot with the alias plt
import matplotlib.pyplot as plt

# Plot the price of stock over time
plt.plot(days, prices, color="red", linestyle="--")

# Display the plot
plt.show()

# Plot price as a function of time
plt.plot(days, prices, color="red", linestyle="--")

# Add x and y labels
plt.xlabel('Days')
plt.ylabel('Prices, $')

# Add plot title
plt.title('Company Stock Prices Over Time')

# Show plot
plt.show()

# Plot two lines of varying colors
plt.plot(days, prices1, color='red')
plt.plot(days, prices2, color='green')

# Add labels
plt.xlabel('Days')
plt.ylabel('Prices, $')
plt.title('Stock Prices Over Time')
plt.show()

# Plot price as a function of time
plt.scatter(x=days, y=prices, color='green', s=0.1)

# Show plot
plt.show()

# Plot histogram
plt.hist(prices, bins=100)

# Display plot
plt.show()

# Plot histogram of stocks_A
plt.hist(stock_A, bins=100, alpha=0.4)

# Plot histogram of stocks_B
plt.hist(stock_B, bins=100, alpha=0.4)

# Display plot
plt.show()

# Plot stock_A and stock_B histograms
plt.hist(stock_A, bins=100, alpha=0.4, label="Stock A")
plt.hist(stock_B, bins=100, alpha=0.4, label="Stock B")

# Add the legend
plt.legend()

# Display the plot
plt.show()

