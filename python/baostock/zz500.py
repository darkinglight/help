import baostock as bs
import pandas as pd
import os


def zz500():
    filename = "data/zz500.csv"
    if os.path.exists(filename):
        result = pd.read_csv(filename, sep=",", encoding='utf-8')
    else:
        rs = bs.query_zz500_stocks()
        zz500_stocks = []
        while (rs.error_code == '0') & rs.next():
            zz500_stocks.append(rs.get_row_data())
        result = pd.DataFrame(zz500_stocks, columns=rs.fields)
        result.to_csv(filename, encoding="utf-8", index=False)
    return result

if __name__ == "__main__":
    lg = bs.login()
    result = zz500()
    bs.logout()
    print(result)
