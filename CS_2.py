# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", list(stocks.keys()))

stock_name = input("Enter stock name: ").upper()

if stock_name in stocks:
    quantity = int(input("Enter quantity: "))

    price = stocks[stock_name]
    total_investment = price * quantity

    print("\nStock:", stock_name)
    print("Price per stock:", price)
    print("Quantity:", quantity)
    print("Total investment value:", total_investment)
else:
    print("❌ Stock not available")
