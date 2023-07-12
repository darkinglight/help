import baostock as bs
import pandas as pd
import os


def hs300():
    filename = "data/hs300.csv"
    if os.path.exists(filename):
        result = pd.read_csv(filename, sep=",", encoding='utf-8')
    else:
        rs = bs.query_hs300_stocks()
        hs300_stocks = []
        while (rs.error_code == '0') & rs.next():
            hs300_stocks.append(rs.get_row_data())
        result = pd.DataFrame(hs300_stocks, columns=rs.fields)
        result.to_csv(filename, encoding="utf-8", index=False)
    return result

if __name__ == "__main__":
    #lg = bs.login()
    result = hs300()
    #bs.logout()
    print(result)
