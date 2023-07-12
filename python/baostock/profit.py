import baostock as bs
import pandas as pd
import os

filename = "data/profile.csv"
df = pd.DataFrame(columns=["code","year"])
if os.path.exists(filename):
    df = pd.read_csv(filename, sep=",", encoding='utf-8')

def profit(code, year, quarter):
    global df
    result = df.loc[(df["code"] == code) & (df["year"] == year)]
    if result.shape[0] > 0:
        return result.iloc[0,:]

    itemfilename = "data/profile_{}_{}_{}.csv".format(code,year,quarter)
    if os.path.exists(itemfilename):
        item = pd.read_csv(itemfilename)
    else:
        rs_profit = bs.query_profit_data(code, year=year, quarter=quarter)
        print("call query_profit-data api", code, year, quaarter)
        data_list = []
        while(rs_profit.error_code == '0') & rs_profit.next():
            data_list.append(rs_profit.get_row_data())
        item = pd.DataFrame(data_list, columns=rs_profit.fields)
    item.insert(1, 'year', year)
    item.insert(2, 'quarter', quarter)
    df = df._append(item)
    df.to_csv(filename, encoding="utf-8", index=False)
    return item.iloc[0,:]

if __name__ == "__main__":
    result = profit("sh.600009", 2022, 4)
    print(result)
