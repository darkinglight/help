import baostock as bs
import pandas as pd
import os


def allstock():
    filename = "data/allstock.csv"
    if os.path.exists(filename):
        result = pd.read_csv(filename, sep=",", encoding='utf-8')
    else:
        rs = bs.query_all_stock(day="2023-07-20")
        hs300_stocks = []
        while (rs.error_code == '0') & rs.next():
            hs300_stocks.append(rs.get_row_data())
        result = pd.DataFrame(hs300_stocks, columns=rs.fields)
        result.to_csv(filename, encoding="utf-8", index=False)
    return result

if __name__ == "__main__":
    lg = bs.login()
    result = allstock()
    bs.logout()
    print(result)
