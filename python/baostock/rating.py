from SqliteTool import SqliteTool
from priceinfo import listPrice
from baseinfo import baseinfo
from profit import profit

if __name__ == "__main__":
    create_tb_sql = ("create table if not exists rating1 ("
                     "code text PRIMARY KEY,"
                     "name text,"
                     "pe float default 0,"
                     "pb float default 0,"
                     "roe2019 float default 0,"
                     "roe2020 float default 0,"
                     "roe2021 float default 0,"
                     "roe2022 float default 0,"
                     "roe2023 float default 0,"
                     "roeAvg float default 0,"
                     "yoyEquity2019 float default 0,"
                     "yoyEquity2020 float default 0,"
                     "yoyEquity2021 float default 0,"
                     "yoyEquity2022 float default 0,"
                     "yoyEquity2023 float default 0,"
                     "yoyEquityAvg float default 0,"
                     "dividendAvg float default 0,"
                     "realGrowth float default 0,"
                     "peg float default 0"
                     ");")
    # 创建对象
    sqliteTool = SqliteTool()
    sqliteTool.drop_table("drop table rating1")
    # 创建数据表
    sqliteTool.create_table(create_tb_sql)

    result = listPrice()
    for price in result:
        base = baseinfo(price.code)
        if int(base.ipoDate[0:4]) >= 2019:
            continue
        p2019 = profit(price.code, 2019, 4)
        if p2019 is None or p2019.yoyEquity <= 0:
            continue
        p2020 = profit(price.code, 2020, 4)
        if p2020 is None or p2020.yoyEquity <= 0:
            continue
        p2021 = profit(price.code, 2021, 4)
        if p2021 is None or p2021.yoyEquity <= 0:
            continue
        p2022 = profit(price.code, 2022, 4)
        if p2022 is None or p2022.yoyEquity <= 0:
            continue
        roeAvg = (p2019.roe + p2020.roe + p2021.roe + p2022.roe) / 4
        yoyEquityAvg = (p2019.yoyEquity + p2020.yoyEquity + p2021.yoyEquity + p2022.yoyEquity) / 4
        sqliteTool.operate_one('insert or replace into rating1 '
                               '(code, name, pe, pb, '
                               'roe2019,roe2020,roe2021,roe2022,roeAvg,'
                               'yoyEquity2019,yoyEquity2020,yoyEquity2021,yoyEquity2022,yoyEquityAvg) '
                               'values(?,?,?,?, ?,?,?,?,?, ?,?,?,?,?) ',
                               (price.code, base.name, price.pe, price.pb,
                                p2019.roe, p2020.roe, p2021.roe, p2022.roe, roeAvg,
                                p2019.yoyEquity, p2020.yoyEquity, p2021.yoyEquity, p2022.yoyEquity, yoyEquityAvg))
