import baostock as bs
import pandas as pd
import os
import math
from baseinfo import baseinfo
from hs300 import hs300
from profit import profit
from priceinfo import priceinfo

if __name__ == '__main__':
    res = pd.DataFrame(columns=('name','growth','pe','peg','roe2022', "roeAvg"))
    hs300 = hs300()
    year = 2022
    quarter = 4
    date = "2023-07-05"
    for index, row in hs300.iterrows():
        if index < 10:
            code = row['code']
            print("code", code)
            base = baseinfo(code)
            print(base)

            price = priceinfo(code, date)
            print("peTTM:", price.loc[price.shape[0] - 1, 'peTTM'])
            
            profit2019 = profit(code, year - 3, quarter)
            profit2020 = profit(code, year - 2, quarter)
            profit2021 = profit(code, year - 1, quarter)
            profit2022 = profit(code, year, quarter)

            earningRate = (profit2022['netProfit'].astype(float)/profit2019['netProfit'].astype(float)).get(0)
            if earningRate > 0:
                avgEarning = math.pow(earningRate, 1/3) * 100 - 100
            else:
                avgEarning = 0

            name = base.iloc[0,1]
            pe = price.loc[price.shape[0] - 1, 'peTTM']
            roe2022 = profit2022.loc[0, 'roeAvg'] * 100
            res = res._append({'name': name, 'growth':avgEarning, 'pe': pe, 'roe2022': roe2022}, ignore_index=True)
    print(res)
    #res.plot.bar()
