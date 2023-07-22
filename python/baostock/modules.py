import baostock as bs
import pandas as pd
import os
import math
import matplotlib.pyplot as plt
from baseinfo import baseinfo
from hs300 import hs300
from zz500 import zz500
from profit import profit
from priceinfo import priceinfo

def getRoeAvg(profit):

    if type(profit['roeAvg']) != 'str':
        return float(profit['roeAvg']) * 100
    elif len(profit['roeAvg']) <= 0:
        return 0
    else:
        return round(float(profit['roeAvg']) * 100,2)

if __name__ == '__main__':
    #lg = bs.login()
    res = pd.DataFrame(columns=('name','netProfit2019','netProfit2022','growth','pe','roe2019','roe2020','roe2021','roe2022', "roeAvg", "roeMin","pb","roe/pb", "score"))
    hs300 = hs300()
    zz500 = zz500()
    zz800 = pd.concat([hs300,zz500], ignore_index=True)
    year = 2022
    quarter = 4
    date = "2023-07-05"
    for index, row in zz800.iterrows():
        if index < 750:
            code = row['code']

            base = baseinfo(code)
            if base["type"] != 1 | base["status"] != 1:
                continue
            name = base.loc["code_name"]

            price = priceinfo(code, date)
            pe = round(float(price.loc['peTTM']),2)
            pb = round(float(price.loc['pbMRQ']),2)
            
            profit2022 = profit(code, year, quarter)
            roe2022 = getRoeAvg(profit2022)
            netProfit2022 = round(float(profit2022['netProfit']),2)
            profit2021 = profit(code, year - 1, quarter)
            roe2021 = getRoeAvg(profit2021)
            profit2020 = profit(code, year - 2, quarter)
            roe2020 = getRoeAvg(profit2020)
            profit2019 = profit(code, year - 3, quarter)
            roe2019 = getRoeAvg(profit2019)
            netProfit2019 = round(float(profit2019['netProfit']),2)
            growth = round((netProfit2022 / netProfit2019 * 100 - 100)/4, 2)
            item = pd.Series({'name':name,'netProfit2019':netProfit2019,'netProfit2022':netProfit2022, 'growth':growth,'pe':pe,'roe2019':roe2019,'roe2020':roe2020,'roe2021':roe2021,'roe2022':roe2022,'pb':pb})
            res = pd.concat([res,item.to_frame().T], ignore_index=True)
    # 过滤负分记录
    minRoe = 10
    res = res.loc[(res["roe2019"] > minRoe) & (res["roe2020"] > minRoe) & (res["roe2021"] > minRoe) & (res["roe2022"] > minRoe) & (res["pe"] > minRoe) & (res["pe"] > 0) & (res["pe"] < 30) & (res["growth"] > 5)]
    res['roeAvg'] = res[['roe2019','roe2020','roe2021','roe2022']].mean(1)
    res['roeMin'] = res[['roe2022','roeAvg']].min(1)
    res['roe/pb'] = res['roeMin'] / res['pb']
    # roe打分
    res = res.sort_values(by = "roeAvg", ascending = False)
    score = 0
    for index, row in res.iterrows():
        score += 1
        res['score'][index] = score
    # pe打分
    res = res.sort_values(by = "pe", ascending = True)
    score = 0
    for index, row in res.iterrows():
        score += 1
        res['score'][index] += score
    
    res = res.sort_values(by = "score", ascending = True)
    res.to_csv("dump.csv", encoding='utf-8')
    #plt.rcParams['font.family'] = 'Microsoft YaHei'
    #res = res.set_index('name')
    #res = res.head(n = 20)
    #ax = res.plot(y = 'roeAvg')
    #res.plot(y='pe', ax=ax)
    #ax.legend()
    #plt.show()
    #bs.logout()
