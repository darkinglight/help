import baostock as bs
import pandas as pd
import os

newfilename = "data/profile.csv"
df = pd.DataFrame()
if os.path.exists(newfilename):
    df = pd.read_csv(newfilename, sep=",", encoding='utf-8')

def profit(code, year, quarter):
    result = df.loc[(df["code"] == code) & (df["year"] == year)]
    if result.shape[0] > 0:
        return result

    filename = "data/profile_{}_{}_{}.csv".format(code,year,quarter)
    if os.path.exists(filename):
        result_profit = pd.read_csv(filename)
    else:
        rs_profit = bs.query_profit_data(code, year=year, quarter=quarter)
        data_list = []
        while(rs_profit.error_code == '0') & rs_profit.next():
            data_list.append(rs_profit.get_row_data())
        result_profit = pd.DataFrame(data_list, columns=rs_profit.fields)
        result_profit.to_csv(filename, encoding="utf-8", index=False)
    return result_profit

if __name__ == "__main__":
    result = profit("sh.600000", 2022, 4)
    print(result)
