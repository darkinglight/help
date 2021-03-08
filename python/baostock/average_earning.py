import baostock as bs
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import math

def get_closeprice(code):
    rs_open = bs.query_profit_data(code, year=2015, quarter=3)
    data_list = []
    while(rs_open.error_code == '0') & rs_open.next():
        data_list.append(rs_open.get_row_data())
    result_open = pd.DataFrame(data_list, columns=rs_open.fields, index=[code])

    rs_close = bs.query_profit_data(code, year=2020, quarter=3)
    data_list = []
    while(rs_close.error_code == '0') & rs_close.next():
        data_list.append(rs_close.get_row_data())
    result_close = pd.DataFrame(data_list, columns=rs_close.fields, index=[code])

    result = pd.merge(result_open, result_close, on="code")
    return result[["code","netProfit_x","netProfit_y"]]

def compute_avg_earning():
    lg = bs.login()

    rs = bs.query_hs300_stocks()
    result = pd.DataFrame()
    while(rs.error_code == '0') & rs.next():
        row = rs.get_row_data()
        code = row[1]
        df = get_closeprice(code)
        df['code_name'] = row[2]
        if result.empty:
            result = df
        else:
            result = result.append(df)
    zz = bs.query_zz500_stocks()
    while(zz.error_code == '0') & zz.next():
        row = zz.get_row_data()
        code = row[1]
        df = get_closeprice(code)
        df['code_name'] = row[2]
        result = result.append(df)
    result = result[result['netProfit_x'] != '']
    result['netProfit_x'] = result['netProfit_x'].astype(float)
    result = result[result['netProfit_x'] > 0]
    result['netProfit_y'] = result['netProfit_y'].astype(float)
    result = result[result['netProfit_y'] > 0]
    result['avgEarningRate'] = (result['netProfit_y']/result['netProfit_x']).apply(lambda x: math.pow(x,1/5)-1)
    result = result.sort_values(by=['avgEarningRate'], ascending=False)
    result.to_csv("avg_earning_rate.csv", encoding="utf-8", index=False)

    result[:10].plot.bar(title='Avg Earning Rate', x='code_name', y='avgEarningRate')
    plt.show()

    bs.logout()

if __name__ == '__main__':
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['font.family']='sans-serif'
    compute_avg_earning()
