import baostock as bs
import pandas as pd
import os
import math

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

def profit(code, year, quarter):
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

def hs300():
    filename = "data/hs300.csv"
    if os.path.exists(filename):
        result = pd.read_csv(filename)
    else:
        rs = bs.query_hs300_stocks()
        hs300_stocks = []
        while (rs.error_code == '0') & rs.next():
            hs300_stocks.append(rs.get_row_data())
        result = pd.DataFrame(hs300_stocks, columns=rs.fields)
        result.to_csv(filename, encoding="utf-8", index=False)
    return result

if __name__ == '__main__':
    res = pd.DataFrame(columns=('name','growth','pe','peg'))
    lg = bs.login()
    hs300 = hs300()
    year = 2020
    quarter = 3
    date = "2021-03-22"
    for index, row in hs300.iterrows():
        code = row['code']
        baseinfo = baseinfo(code)

        priceinfo = priceinfo(code, date)
        print("peTTM:", priceinfo.loc[priceinfo.shape[0] - 1, 'peTTM'])
        
        profitMid = profit(code, year - 3, quarter)
        profitPost = profit(code, year, quarter)
        avgEarning3 = (profitPost['netProfit'].astype(float)/profitMid['netProfit'].astype(float)).apply(lambda x: math.pow(x,1/3)-1)
        res = res.append([{'name':baseinfo.loc[0, 'code_name'],'growth':avgEarning3.get(0)*100, 'pe':priceinfo.loc[priceinfo.shape[0] - 1]}], ignore_index=True)
    print(res)
    bs.logout()
