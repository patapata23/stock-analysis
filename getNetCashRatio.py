import yfinance as yf
import pandas as pd

def get_net_cash_ratio(ticker):
    # ティッカーシンボルから企業情報を取得
    company = yf.Ticker(ticker)
    
    # 最新の四半期データを取得
    #financials = company.quarterly_financials
    balance_sheet = company.quarterly_balance_sheet
    # print(balance_sheet.tail(50))

    # 銘柄名を取得
    company_name = company.info['longName']

    # 時価総額を取得
    market_cap = company.info['marketCap']
    # 時価総額20億以下はネットキャッシュ率0に決め打ちして、計算省略
    if market_cap < 2000000000 | market_cap > 20000000000 :
        return 0

    net_cash = 0
    try: 
        # 最新の四半期の流動資産、投資有価証券、負債を取得
        current_assets = balance_sheet.loc['Current Assets', :].iloc[0]
        investments = balance_sheet.loc['Available For Sale Securities', :].iloc[0]
        total_liabilities = balance_sheet.loc['Total Debt', :].iloc[0]
    
        # ネットキャッシュを計算
        net_cash = current_assets + investments * 0.7 - total_liabilities
    except:
        pass
    return ticker, company_name, net_cash/market_cap

# ティッカーリストを作成
df_codes = pd.read_csv('jpx_code.csv')
# codes_list = df_codes['コード'].tolist()
codes_list = df_codes['コード'].tolist()[0:100]

# ネットキャッシュをスクリーニング
results = []
for code in codes_list:
    try:
        ticker = str(code) + '.T'
        ticker, company_name, net_cash_ratio = get_net_cash_ratio(ticker)
        if net_cash_ratio >= 1:
            # 結果を出力
            print(f"{ticker} ({company_name}) のネットキャッシュ率: {net_cash_ratio:,.2f}")
            results.append((ticker, company_name, net_cash_ratio))
    except:
        pass
    
# CSVファイルに出力
df = pd.DataFrame(results, columns=['Ticker', 'Company Name', 'Net Cash Ratio'])
df.to_csv('net_cash_ratio_results.csv', index=False)