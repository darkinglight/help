import baostock as bs
import pandas as pd
import os


filename = "data/priceinfo.csv"
df = pd.DataFrame(columns=["code"])
if os.path.exists(filename):
    df = pd.read_csv(filename, sep=",", encoding='utf-8')

def priceinfo(code, date):
    global df
    result = df.loc[df["code"] == code]
    if result.shape[0] > 0:
        return result.iloc[0,:]

    itemfilename = "data/priceinfo_{}.csv".format(code)
    if os.path.exists(itemfilename):
        item = pd.read_csv(itemfilename)
    else:
        rs = bs.query_history_k_data_plus(code, "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM", start_date=date,frequency="d", adjustflag="3")
        result_list = []
        while (rs.error_code == '0') & rs.next():
            result_list.append(rs.get_row_data())
        item = pd.DataFrame(result_list, columns=rs.fields)

    df = df.append(item)
    df.to_csv(filename, encoding="utf-8", index=False)
    return item.iloc[0,:]

if __name__ == "__main__":
    result = priceinfo("sh.600009","2023-07-05")
    print(result)
