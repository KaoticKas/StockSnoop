from asyncio.windows_events import NULL
import dataStream as dS
import datetime as dt

if __name__ =="__main__":
    print("")
    ticker = ""

    while len(ticker) < 4:
     ticker = input("Please Enter the stock you want to analyse: ")

    dateInput = input("Please enter a Start date in YYYY-MM-DD Format: ")
    year,month,day = map(int, dateInput.split('-'))
    startDate = dt.date(year,month,day)

    dateInput = input("Please enter a End date in YYYY-MM-DD Format: ")
    year,month,day = map(int, dateInput.split('-'))
    endDate = dt.date(year,month,day)

    data = dS.stockInfo(ticker,startDate,endDate)
    print(data)