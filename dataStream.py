import pandas_datareader as pdr
import datetime as dt
if __name__ == '__main__':
    print("hello world")


def stockInfo(stockName, timeFrameStart, TimeFrameEnd):
    startFrame = timeFrameStart
    endFrame = TimeFrameEnd
    stock = stockName
    data = pdr.get_data_yahoo(stock, startFrame, endFrame)

    return data
