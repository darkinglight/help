import baostock as bs
import pandas as pd
import os
import math
from baseinfo import baseinfo
from hs300 import hs300
from profit import profit
from priceinfo import priceinfo

if __name__ == '__main__':
    lg = bs.login()
    res = pd.DataFrame(columns=('name','growth','pe','peg','roe2022', "roeAvg", "score"))
    hs300 = hs300()
    year = 2022
    quarter = 4
    date = "2023-07-05"
    for index, row in hs300.iterrows():
        if index < 50:
            code = row['code']
            print(code)
            base = baseinfo(code)

            price = priceinfo(code, date)
            print("peTTM:", price.loc['peTTM'])
            
            profit2019 = profit(code, year - 3, quarter)
            profit2020 = profit(code, year - 2, quarter)
            profit2021 = profit(code, year - 1, quarter)
            profit2022 = profit(code, year, quarter)

            pe = float(price.loc['peTTM'])
            peg = 0
            earningRate = float(profit2022['netProfit'])/float(profit2019['netProfit'])
            if earningRate > 0:
                avgEarning = math.pow(earningRate, 1/3) * 100 - 100
                peg = pe / avgEarning
            else:
                avgEarning = 0

            name = base.loc["code_name"]
            roe2022 = float(profit2022['roeAvg']) * 100
            roeAvg = (float(profit2019['roeAvg']) + float(profit2020['roeAvg']) + float(profit2021['roeAvg']) + float(profit2022['roeAvg'])) * 100 / 4
            res = res.append({'name': name, 'growth': round(avgEarning,2), 'pe': round(pe,2), 'peg': round(peg,2), 'roe2022': round(roe2022,2), 'roeAvg': round(roeAvg,2)}, ignore_index=True)
    # 过滤负分记录
    res = res.loc[(res["roeAvg"] > 0) & (res["pe"] > 0)]
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
    bs.logout()
