import baostock as bs
import pandas as pd
import os
import math
from baseinfo import baseinfo
from hs300 import hs300
from profit import profit
from priceinfo import priceinfo

def getRoeAvg(profit):

    if type(profit['roeAvg']) != 'str':
        return profit['roeAvg']
    elif len(profit['roeAvg']) <= 0:
        return 0
    else:
        return round(float(profit['roeAvg']) * 100,2)

if __name__ == '__main__':
    #lg = bs.login()
    res = pd.DataFrame(columns=('name','netProfit2019','netProfit2022','growth','pe','peg','roe2019','roe2020','roe2021','roe2022', "roeAvg", "score"))
    hs300 = hs300()
    year = 2022
    quarter = 4
    date = "2023-07-05"
    for index, row in hs300.iterrows():
        if index < 10:
            code = row['code']

            base = baseinfo(code)
            name = base.loc["code_name"]

            price = priceinfo(code, date)
            pe = round(float(price.loc['peTTM']),2)
            
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
            item = pd.Series({'name':name,'netProfit2019':netProfit2019,'netProfit2022':netProfit2022,'pe':pe,'roe2019':roe2019,'roe2020':roe2020,'roe2021':roe2021,'roe2022':roe2022})
            res = pd.concat([res,item.to_frame().T], ignore_index=True)
    # 过滤负分记录
    res = res.loc[(res["roe2019"] > 0) & (res["roe2020"] > 0) & (res["roe2021"] > 0) & (res["roe2022"] > 0) & (res["pe"] > 0)]
    res['roeAvg'] = res[['roe2019','roe2020','roe2021','roe2022']].mean(1)
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
    print(res)
    res.to_csv("dump.csv", encoding='utf-8')
    #res.plot.bar()
    #bs.logout()
