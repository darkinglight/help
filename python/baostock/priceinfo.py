import baostock as bs
import pandas as pd
import os


def priceinfo(code, date):
    filename = "data/priceinfo_{}.csv".format(code)
    if os.path.exists(filename):
        result = pd.read_csv(filename)
    else:
        rs = bs.query_history_k_data_plus(code, "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM", start_date=date,frequency="d", adjustflag="3")
        result_list = []
        while (rs.error_code == '0') & rs.next():
            result_list.append(rs.get_row_data())
        result = pd.DataFrame(result_list, columns=rs.fields)
        result.to_csv(filename, encoding="utf-8", index=False)
    return result


