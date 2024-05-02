import requests
import pandas as pd

url = "https://www.jpx.co.jp/markets/statistics-equities/misc/tvdivq0000001vg2-att/data_j.xls"
r = requests.get(url)
with open('data_j.xls', 'wb') as output:
    output.write(r.content)
stocklist = pd.read_excel("./data_j.xls")
stocklist.loc[stocklist["市場・商品区分"]=="市場第一部（内国株）",
              ["コード","銘柄名","33業種コード","33業種区分","規模コード","規模区分"]
             ]

# ETF等を除く
codes = stocklist[(stocklist['市場・商品区分'] == 'プライム（内国株式）') | (stocklist['市場・商品区分'] == 'スタンダード（内国株式）')]
len(codes) 

codes.to_csv('jpx_code.csv')
