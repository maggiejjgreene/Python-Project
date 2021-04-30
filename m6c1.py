# Calculate the future value of the investment and print it out
future_value = 100*(1+0.06)**30
print("Future Value of Investment: " + str(round(future_value, 2)))

# Predefined variables
initial_investment = 100
growth_periods = 30
growth_rate = 0.06

# Calculate the value for the investment compounded once per year
compound_periods_1 = 1
investment_1 = initial_investment*(1 + growth_rate / compound_periods_1)**(compound_periods_1*growth_periods)
print("Investment 1: " + str(round(investment_1, 2)))

# Calculate the value for the investment compounded quarterly
compound_periods_2 = 4
investment_2 = initial_investment*(1 + growth_rate / compound_periods_2)**(compound_periods_2*growth_periods)
print("Investment 2: " + str(round(investment_2, 2)))

# Calculate the value for the investment compounded monthly
compound_periods_3 = 12
investment_3 = 100*(1+0.06/12)**(12*30)
print("Investment 3: " + str(round(investment_3, 2)))

# Calculate the future value
initial_investment = 100
growth_rate = -0.05
growth_periods = 10
future_value = initial_investment*(1 + growth_rate)**(growth_periods)
print("Future value: " + str(round(future_value, 2)))

# Calculate the discount factor
discount_factor = 1/((1 + growth_rate)**(growth_periods))
print("Discount factor: " + str(round(discount_factor, 2)))

# Derive the initial value of the investment
initial_investment_again = 100*(1+-0.05)**10 * 1/(1+-0.05)**10
print("Initial value: " + str(round(initial_investment_again, 2)))

# Import numpy as np
import numpy as np

import numpy_financial as npf

# Calculate investment_1
investment_1 = npf.pv(rate=0.03, nper=15, pmt=0, fv=10000)

# Note that the present value returned is negative, so we multiply the result by -1
print("Investment 1 is worth " + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = npf.pv(rate=0.05, nper=10, pmt=0, fv=10000)
print("Investment 2 is worth " + str(round(-investment_2, 2)) + " in today's dollars")


import numpy_financial as npf

# Calculate investment_1
investment_1 = npf.fv(rate=0.05, nper=15, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 15 years")

# Calculate investment_2
investment_2 = npf.fv(rate=0.08, nper=15, pmt=0, pv=-10000)
print("Investment 2 will yield a total of $" + str(round(investment_2, 2)) + " in 15 years")

import numpy as np
import numpy_financial as npf

# Calculate investment_1
investment_1 = npf.fv(rate=0.08, nper=10, pmt=0, pv=-10000)
print("Investment 1 will yield a total of $" + str(round(investment_1, 2)) + " in 10 years")

# Calculate investment_2
investment_1_discounted = npf.pv(rate=0.03, nper=10, pmt=0, fv=21589.24997272788)
print("After adjusting for inflation, investment 1 is worth $" + str(round(-investment_1_discounted, 2)) + " in today's dollars")

import numpy as np
import numpy_financial as npf

# Predefined array of cash flows
cash_flows = np.array([100, 100, 100, 100, 100])

# Calculate investment_1
investment_1 = npf.npv(rate=0.03, values=np.array([100,100,100,100,100]))
print("Investment 1's net present value is $" + str(round(investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = npf.npv(rate=0.05, values=np.array([100,100,100,100,100]))
print("Investment 2's net present value is $" + str(round(investment_2, 2)) + " in today's dollars")

# Calculate investment_3
investment_3 = npf.npv(rate=0.07, values=np.array([100,100,100,100,100]))
print("Investment 3's net present value is $" + str(round(investment_3, 2)) + " in today's dollars")

import numpy as np
import numpy_financial as npf

# Create an array of cash flows for project 1
cash_flows_1 = np.array([-250,100,200,300,400])

# Create an array of cash flows for project 2
cash_flows_2 = np.array([-250,300,-250,300,300])

# Calculate the net present value of project 1
investment_1 = npf.npv(rate=0.03, values=np.array([-250,100,200,300,400]))
print("The net present value of Investment 1 is worth $" + str(round(investment_1, 2)) + " in today's dollars")

# Calculate the net present value of project 2
investment_2 = npf.npv(rate=0.03, values=([-250,300,-250,300,300]))
print("The net present value of Investment 2 is worth $" + str(round(investment_2, 2)) + " in today's dollars")

import numpy as np
import numpy_financial as npf

# Calculate investment_1
investment_1 = npf.pv(rate=0.03, nper=30, pmt=0, fv=100)
print("Investment 1 is worth $" + str(round(-investment_1, 2)) + " in today's dollars")

# Calculate investment_2
investment_2 = npf.pv(rate=0.03, nper=50, pmt=0, fv=100)
print("Investment 2 is worth $" + str(round(-investment_2, 2)) + " in today's dollars")

# Calculate investment_3
investment_3 = npf.pv(rate=0.03, nper=100, pmt=0, fv=100)
print("Investment 3 is worth $" + str(round(-investment_3, 2)) + " in today's dollars")

