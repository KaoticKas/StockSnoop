import pandas_datareader as pdr
import datetime as dt
if __name__ == '__main__':
    start = dt.datetime(2022, 8, 26)
    data = pdr.get_data_yahoo("NG=F",start)

    print(data.head())