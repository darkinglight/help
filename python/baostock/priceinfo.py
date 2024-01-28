import baostock as bs
import pandas as pd
import os


def priceinfo(code, date):
    result = df.loc[df["code"] == code]
    if result.shape[0] <= 0:
        rs = bs.query_history_k_data_plus(code, "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM", start_date=date,frequency="d", adjustflag="3")
        result_list = []
        while (rs.error_code == '0') & rs.next():
            result_list.append(rs.get_row_data())
        result = pd.DataFrame(result_list, columns=rs.fields)
        df = pd.concat([df, result])
        df.to_csv(filename, encoding="utf-8", index=False)
    if result.shape[0] <= 0:
        omit = pd.Series([date,code,-1,-1,-1,-1,-1],index=['date','code','close','peTTM','pbMRQ','psTTM','pcfNcfTTM'])
        df = pd.concat([df,omit.to_frame().T],ignore_index=True)
        df.to_csv(filename, encoding="utf-8", index=False)
        return omit
    return result.iloc[0]

if __name__ == "__main__":
    date = '2023-07-05'
    result = priceinfo("sh.600009","2023-07-05")
    print(result)
