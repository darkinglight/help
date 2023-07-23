import baostock as bs
import pandas as pd
import os


filename = "data/baseinfo.csv"
df = pd.DataFrame()
if os.path.exists(filename):
    df = pd.read_csv(filename, sep=",", encoding='utf-8')

def baseinfo(code):
    global df
    result = df.loc[df["code"] == code]
    if result.shape[0] <= 0:
        rs = bs.query_stock_basic(code=code)
        data_list = []
        while(rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        if result.shape[0] <= 0:
            omit = pd.Series([code, -1, -1], index=['code','type','status'])
            result = pd.concat([result,omit.to_frame().T],ignore_index=True)
        df = pd.concat([df,result])
        df.to_csv(filename, encoding="utf-8", index=False)
    return result.iloc[0]

if __name__ == "__main__":
    from allstock import allstock
    import sys
    lg = bs.login()
    allstock = allstock()
    for index, row in allstock.iterrows():
        if index < 10000:
            code = row['code']
            baseinfo(code)
            print(code)
    bs.logout()

    #code = "bj.430017"
    #if len(sys.argv) > 1:
    #    code = sys.argv[1]
    #lg = bs.login()
    #result = baseinfo(code)
    #bs.logout()
    #print(result)
