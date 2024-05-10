from SqliteTool import SqliteTool
from priceinfo import listPrice
from baseinfo import baseinfo
from profit import profit
from dupon import dupont

# peg's pe use peAvg = pb/roeAvg
if __name__ == "__main__":
    create_tb_sql = ("create table if not exists rating1 ("
                     "code text PRIMARY KEY,"
                     "name text,"
                     "pe float default 0,"
                     "pb float default 0,"
                     "roe2020 float default 0,"
                     "roe2021 float default 0,"
                     "roe2022 float default 0,"
                     "roe2023 float default 0,"
                     "roeAvg float default 0,"
                     "yoyEquity2020 float default 0,"
                     "yoyEquity2021 float default 0,"
                     "yoyEquity2022 float default 0,"
                     "yoyEquity2023 float default 0,"
                     "yoyEquityAvg float default 0,"
                     "dividendAvg float default 0,"
                     "realGrowth float default 0,"
                     "peg float default 0,"
                     "assetToEquity float default 0,"
                     "peAvg float default 0,"
                     "pegAvg float default 0"
                     ");")
    # 创建对象
    sqliteTool = SqliteTool()
    sqliteTool.drop_table("drop table rating1")
    # 创建数据表
    sqliteTool.create_table(create_tb_sql)

    result = listPrice()
    for price in result:
        base = baseinfo(price.code)
        if int(base.ipoDate[0:4]) >= 2020:
            continue
        p2020 = profit(price.code, 2020, 4)
        if p2020 is None:
            continue
        p2021 = profit(price.code, 2021, 4)
        if p2021 is None:
            continue
        p2022 = profit(price.code, 2022, 4)
        if p2022 is None:
            continue
        p2023 = profit(price.code, 2023, 4)
        if p2023 is None:
            continue
        roeAvg = (p2020.roe + p2021.roe + p2022.roe + p2023.roe) * 100 / 4
        yoyEquityAvg = (p2020.yoyEquity + p2021.yoyEquity + p2022.yoyEquity + p2023.yoyEquity) * 100 / 4
        dividendAvg = roeAvg - yoyEquityAvg
        realGrowth = dividendAvg / price.pb + yoyEquityAvg
        peg = price.pe / realGrowth
        peAvg = price.pb / roeAvg
        pegAvg = peAvg * 100 / realGrowth
        dupon = dupont(price.code)
        sqliteTool.operate_one('insert or replace into rating1 '
                               '(code, name, pe, pb, '
                               'roe2020,roe2021,roe2022,roe2023,roeAvg,'
                               'yoyEquity2020,yoyEquity2021,yoyEquity2022,yoyEquity2023,yoyEquityAvg,'
                               'dividendAvg,realGrowth,peg,assetToEquity,peAvg,pegAvg) '
                               'values(?,?,?,?, ?,?,?,?,?, ?,?,?,?,?, ?,?,?,?, ?,?) ',
                               (price.code, base.name, price.pe, price.pb,
                                p2020.roe, p2021.roe, p2022.roe, p2023.roe, roeAvg,
                                p2020.yoyEquity, p2021.yoyEquity, p2022.yoyEquity, p2023.yoyEquity, yoyEquityAvg,
                                dividendAvg, realGrowth, peg, dupon.dupontAssetStoEquity,
                                peAvg * 100, pegAvg))
