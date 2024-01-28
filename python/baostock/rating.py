from SqliteTool import SqliteTool
from priceinfo import listPrice
from baseinfo import baseinfo

if __name__ == "__main__":
    create_tb_sql = ("create table if not exists rating1 ("
                     "code text PRIMARY KEY,"
                     "name text"
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
        name = baseinfo(price.code).name
        # print(name, price.pe, price.pb, '\n')
        sqliteTool.operate_one('insert or replace into rating1 (code, name) values(?,?) ',
                               (price.code, name))
