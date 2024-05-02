from pprint import pprint
import pandas as pd
import yfinance as yf
# JALの情報を取得
ticker_info = yf.Ticker("9201.T")
df_bs=ticker_info.balance_sheet/100000000   #貸借対照表 1億円単位にします。

df_bs['acct']=df_bs.index#Indexにある勘定科目を列にもってくる
df_bs=df_bs.set_axis(['23/03/31', '23/03/31', '21/03/31','acct'], axis='columns')#コラム名の変更

#自前で日本語変換用のテーブルを作成しました。
#日本語化のためのテーブル作成
code=({
    'acct':['Cash','Net Receivables','Short Term Investments','Inventory','Other Current Assets','Property Plant Equipment','Intangible Assets','Good Will','Long Term Investments','Deferred Long Term Asset Charges','Other Assets','Total Assets','Total Current Assets','Total Liab','Total Current Liabilities','Accounts Payable','Other Current Liab','Short Long Term Debt','Long Term Debt','Other Liab','Common Stock','Capital Surplus','Retained Earnings','Other Stockholder Equity','Total Stockholder Equity','Minority Interest','Net Tangible Assets','Gains Losses Not Affecting Retained Earnings'],
'財務諸表項目':['流動資産項目','流動資産項目','流動資産項目','流動資産項目','流動資産項目','固定資産項目','固定資産項目','固定資産項目','固定資産項目','固定資産項目','固定資産項目','総資産合計','流動資産合計','負債合計','流動負債合計','流動負債項目','流動負債項目','流動負債項目','固定負債項目','固定負債項目','純資産項目','純資産項目','純資産項目','純資産項目','純資産','純資産','純資産項目','純資産項目'],
'財務諸表項目明細':['現金及び現金同等物','営業債権及びその他の債権','その他の金融資産','棚卸資産','その他の流動資産','有形固定資産','無形資産','のれん','長期保有目的の投資等','繰り延べ税金資産','その他金融資産合計','総資産合計','流動資産合計','負債合計','流動負債合計','売掛金','短期有利子負債','その他金融資産','長期負債','その他の長期負債','資本金','資本剰余金','利益剰余金','その他の包括利益','親会社の所有者に帰属する持分合計','非支配持分','純有形資産','その他の包括利益'],
    'order':[6,7,8,9,10,11,13,14,15,16,17,1,0,3,2,18,19,20,21,22,23,24,25,26,4,5,12,27
]
})
code=pd.DataFrame(code)

#mergeして日本語名称をのせる
df2=pd.merge(df_bs,code,left_on='acct',right_on='acct',how='left')
df2.sort_values('order')
df2[['order','財務諸表項目','財務諸表項目明細','acct', '23/03/31', '23/03/31', '21/03/31']].sort_values('order')
#mergeして日本語名称をのせる
df2=pd.merge(df_bs,code,left_on='acct',right_on='acct',how='left')
df2.sort_values('order')
df2[['order','財務諸表項目','財務諸表項目明細','acct', '23/03/31', '23/03/31', '21/03/31']].sort_values('order')

pprint(df2)