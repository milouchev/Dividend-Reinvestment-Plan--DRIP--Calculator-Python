# A simple employee dividend reinvestment plan (DRIP) calculator that shows the growth of an investment in a stock over time

import yfinance as yf
from prettytable import PrettyTable

# Setting up table with columns
myTable = PrettyTable()
myTable.field_names = ["Year","Start Balance","Share Price","Shares","Contribution","Growth","Dividends","Reinvested","End Balance"]

# Getting user inputs
stock = yf.Ticker(input("Enter the stock symbol/ticker: ")).info
stock_price = stock["regularMarketPrice"]
initial = float(input("\nHow many shares do you own? If none, enter 0: "))
lump = float(input("\nWill you be making a lump-sum purchase? If yes, enter the currency amount ($). If no, enter 0: "))
shares = round(initial + (lump/stock_price),2)
balance = round(((initial*stock_price) + lump),2)
monthly_contribution = float(input("\nEnter your monthly contribution ($): "))
yearly_contribution = round(monthly_contribution*12,2)
years = int(input("\nEnter the number of years you will be investing: "))
growth_rate = float(input("\nEnter the expected yearly growth rate in stock price (in percent): "))
growth = round(balance*(growth_rate/100),2)
dividend_yield = float(input("\nEnter the current dividend yield (in percent): "))
dividend_yield_growth = float(input("\nEnter the expected yearly dividend growth rate (in percent): "))
dividends = round(balance*(dividend_yield/100),2)
tax_rate = float(input("\nIs this taxable? If yes, enter the tax rate (in percent). If no, enter 0: " ))
reinvested = round(dividends*(1-(tax_rate/100)),2)
end_balance = round(balance+yearly_contribution+growth+reinvested,2)

# Year 1 table data
myTable.add_row([1, balance, stock_price, shares, yearly_contribution, growth, dividends, reinvested, end_balance])
    
# Setting up iterations
for i in range(2,years+1):
    balance = end_balance
    stock_price_iteration = round(stock_price*(1+(growth_rate/100))**(i-1),2)
    shares_iteration = round(balance/stock_price_iteration,2)
    growth_iteration = round(balance*(growth_rate/100),2)
    dividends = round((stock_price_iteration*shares)*(dividend_yield/100),2)
    reinvested = round(dividends*(1-(tax_rate/100)),2)
    end_balance = round(balance+yearly_contribution+growth_iteration+reinvested,2)
    myTable.add_row([i,+\
                    balance,+\
                    stock_price_iteration,+\
                    shares_iteration,+\
                    yearly_contribution,+\
                    growth_iteration,+\
                    dividends,+\
                    reinvested,+\
                    end_balance])

# Printing table
myTable.header = True
myTable.border = True
print("\n\n"+stock["longName"])
print(myTable)
