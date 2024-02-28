# import modules and libraries
import requests
import json # to parse data as dictionary
s = 'w' # stopping conditions
l = [] # used to store list of stock symbols
print("......................... Welcome tho stock portfolio.................................")
print(".........................created with care by deep sarkar............................")
while s!='q':
    stock_symbol = input("Enter the stock symbol you want to enter to the portfolio(press q to quit):-")
    if stock_symbol == 'q':
        s = 'q'
        break
    else:
        l.append(stock_symbol)
# print the stock symbol :
print("your saved stoc details are :-")
print(l) # display all the stock

# find the stock details from the list which you want to find the details:-
p = 't'
try:
    while p != 'w':
        find_stock = input("Enter the stock from the list you want to find the details(w to break):-")
        for j in range(len(l)):
            if l[j] == find_stock:
                print(f".........................displaying details of the {find_stock} stock..............................")
                r = (requests.get(
                    f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={l[j]}&interval=5min&apikey=your api key'))
                stock_str = json.loads(r.text)
                last_refreshed = (stock_str["Meta Data"]["3. Last Refreshed"])
                print(f"{find_stock} was last refreshed at {last_refreshed}")
                print(stock_str["Time Series (5min)"][last_refreshed])
            if find_stock == "w" or find_stock == "W":
                p = "w"
                break
except Exception as e:
    print(f"stock not found......")
print("Thank you for using stock portfolio.........")

