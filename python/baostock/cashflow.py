import baostock as bs
import pandas as pd
import os

filename = "data/cashflow.csv"
df = pd.DataFrame(columns=["code"])
if os.path.exists(filename):
    df = pd.read_csv(filename, sep=",", encoding='utf-8')

def cashflow(code):
    global df
    item = df.loc[(df["code"] == code)]
    if item.shape[0] <= 0:
        rs_cash_flow = bs.query_cash_flow_data(code,year='2023',quarter='1')
        data_list = []
        while(rs_cash_flow.error_code == '0') & rs_cash_flow.next():
            data_list.append(rs_cash_flow.get_row_data())
        item = pd.DataFrame(data_list, columns=rs_cash_flow.fields)
        print(item)
        df = pd.concat([df,item])
        df.to_csv(filename, encoding="utf-8", index=False)
    if item.shape[0] <= 0:
        omit = pd.Series([code,-1,-1,-1,-1,-1,-1,-1], index = ['code', 'CAToAsset', 'NCAToAsset', 'tangibleAssetToAsset', 'ebitToInterest', 'CFOToOR', 'CFOToNP', 'CFOToGr'])
        df = pd.concat([df,omit.to_frame().T],ignore_index=True)
        df.to_csv(filename, encoding="utf-8", index=False)
        return omit
        
    return item.iloc[0]

if __name__ == "__main__":
    from allstock import allstock
    import sys
    lg = bs.login()
    allstock = allstock()
    for index, row in allstock.iterrows():
        if index < 10000:
            code = row['code']
            cashflow(code)
            print(code)
    bs.logout()


