from pprint import pprint
import pandas_datareader.data as web
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import mplfinance as mf

 
yf.pdr_override()

code = '7203.T'

# df = web.DataReader(code, data_source='yahoo', start='2022-01-01')
# df = web.get_data_yahoo(tickers=code,start='2022-01-01')
# pprint(df.tail())


df_codes = pd.read_csv('jpx_code.csv')
codes_list = df_codes['コード'].tolist()
len(codes_list)

# ソフトバンクグループの情報を取得（Tは東証を表す）
ticker_info = yf.Ticker("9984.T")


# pprint(ticker_info.quarterly_cashflow)
# pprint(ticker_info.financials)

def data_read(code, startdate):
    code2 = str(code) + '.T'
    df = web.get_data_yahoo(tickers=code2,start=startdate)
    #df = web.DataReader(code2, data_source='yahoo', start=startdate)
    df['code'] = code
    return (df)

df = data_read(7203, '2024-04-01')
df.to_csv( "y_stock_data.csv")


start = '2024-01-01'
end = '2024-05-01'
hist = yf.download(tickers="9984.T", start=start, end=end, interval='1d', auto_adjust=True)
# auto_adjust：『始値 / 高値 / 安値 / 終値』の四本値を自動的に調整する

#グラフの表示
chart = mf.plot(hist,style='yahoo',type='candle',title='9984.T Average CHart')
