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


def baseinfo(code):
    filename = "data/baseinfo_{}.csv".format(code)
    if os.path.exists(filename):
        result = pd.read_csv(filename)
    else:
        rs = bs.query_stock_basic(code="sh.601012")
        data_list = []
        while(rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        result.to_csv(filename, encoding="utf-8", index=False)
    return result

def dupont(code, year, quarter):
    filename = "data/dupont_{}_{}_{}.csv".format(code,year,quarter)
    
    if os.path.exists(filename):
        # get from local
        result_profile = pd.read_csv(filename)
    else:
        # get from remote
        dupont_list = []
        rs_dupont = bs.query_dupont_data(code=code, year=year, quarter=quarter)
        while (rs_dupont.error_code == '0') & rs_dupont.next():
            dupont_list.append(rs_dupont.get_row_data())
        result_profile = pd.DataFrame(dupont_list, columns=rs_dupont.fields)
        result_profile.to_csv(filename, encoding="utf-8", index=False)
    return result_profile

if __name__ == '__main__':
    lg = bs.login()
    code = "sh.601012"
    year = 2020
    quarter = 3
    result = dupont(code, year, quarter)
    print(result)
    result = baseinfo(code)
    print(result)
    result = priceinfo(code, "2021-03-22")
    print(result.loc[0, 'peTTM'])
    bs.logout()
