import baostock as bs
import pandas as pd
import os

filename = "data/profile.csv"
df = pd.DataFrame(columns=["code","year"])
if os.path.exists(filename):
    df = pd.read_csv(filename, sep=",", encoding='utf-8')

def profit(code, year, quarter):
    global df
    item = df.loc[(df["code"] == code) & (df["year"] == year)]
    if item.shape[0] <= 0:
        rs_profit = bs.query_profit_data(code, year=year, quarter=quarter)
        data_list = []
        while(rs_profit.error_code == '0') & rs_profit.next():
            data_list.append(rs_profit.get_row_data())
        item = pd.DataFrame(data_list, columns=rs_profit.fields)
        print("call query_profit-data api", code, year, quarter, item)
        item.insert(1, 'year', year)
        item.insert(2, 'quarter', quarter)
        df = pd.concat([df,item])
        df.to_csv(filename, encoding="utf-8", index=False)
    if item.shape[0] <= 0:
        omit = pd.Series([code,year,quarter,-1,-1,-1,-1,-1,-1,-1,-1], index = ['code','year','quarter', 'roeAvg', 'npMargin', 'gpMargin', 'netProfit', 'epsTTM', 'MBRevenue', 'totalShare', 'liqaShare'])
        df = pd.concat([df,omit.to_frame().T],ignore_index=True)
        df.to_csv(filename, encoding="utf-8", index=False)
        return omit
        
    return item.iloc[0]

if __name__ == "__main__":
    result = profit("sh.600009", 2022, 4)
    print(result)
