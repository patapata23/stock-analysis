import pandas as pd
import numpy as np
import datetime

import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

df_codes = pd.read_csv('jpx_code.csv')
codes_list = df_codes['コード'].astype('int64').tolist()

cols = ['datetime', 'open', 'high', 'low', 'close', 'volume', 'code', 'timestamp']
df = pd.DataFrame(index=[], columns=cols)
df = df.set_index('datetime')

error_list = []
for code in codes_list:
    code = str(code) + '.T'
    my_share =share.Share(code)
    symbol_data = None
    
    try:
        symbol_data = my_share.get_historical(
            share.PERIOD_TYPE_DAY,0,
            share.FREQUENCY_TYPE_DAY, 1)
        
        df1 = pd.DataFrame(symbol_data)
        
        try:
            df1['datetime'] = pd.to_datetime(df1.timestamp, unit = 'ms') + datetime.timedelta(hours = 9)
            df1['code'] = code
            df1.set_index('datetime', inplace = True)

            df = pd.concat([df, df1], axis = 0)
        except:
            error_list.append(code)
            
    except YahooFinanceError as e:
            print(e.message)
            print(code)
            error_list.append(code)

today = max(df.index)
fname = today.strftime('%y%m%d')

df.to_csv(fname + '_daily_value_yahoo_tmp.csv')

