from collections import namedtuple

import baostock as bs
import pandas as pd
import os

from SqliteTool import SqliteTool

Profit = namedtuple("Profit", ['code', 'year', 'quarter',
                               'netProfit', 'roe', 'eps', 'share','yoyEquity'])


def profit(code, year, quarter):
    sqliteTool = SqliteTool()
    data = sqliteTool.query_one("select * from profit where code = :code "
                                "and year = :year and quarter = :quarter",
                                {"code": code, "year": year, "quarter": quarter})
    if data == None:
        return data
    dto = Profit(code=data[0], year=data[1], quarter=data[2], netProfit=data[3],
                 roe=data[4], eps=data[5], share=data[6], yoyEquity=data[7])
    return dto


if __name__ == "__main__":
    # 创建数据表dividend的SQL语句
    create_tb_sql = ("create table if not exists profit ("
                     "id INTEGER PRIMARY KEY,"
                     "code text,"
                     "year int,"
                     "quarter int,"
                     "netProfit float default 0,"
                     "roe float default 0,"
                     "eps float default 0,"
                     "share int default 0,"
                     "yoyEquity float default 0,"
                     "UNIQUE(code, year, quarter)"
                     ");")
    # 创建对象
    sqliteTool = SqliteTool()
    # sqliteTool.drop_table("drop table profit")
    # 创建数据表
    sqliteTool.create_table(create_tb_sql)

    from allstock import allstock
    from baseinfo import baseinfo

    stocks = allstock()
    bs.login()
    for stock in stocks:
        base_data = baseinfo(stock.code)
        if base_data.type != 1:
            continue
        for year in range(2015, 2023):
            if year < int(base_data.ipoDate[0:4]):
                continue
            exist = profit(stock.code, year, 4)
            if exist is not None:
                continue
            yoyEquity = 0
            rs = bs.query_growth_data(code=stock.code, year=year, quarter=4)
            if rs.error_code != '0':
                print(stock.code, "get growth error", rs.error_msg)
            while rs.next():
                item = rs.get_row_data()
                yoyEquity = item[3]
            rs = bs.query_profit_data(code=stock.code, year=year, quarter=4)
            if rs.error_code != '0':
                print(stock.code, "get profit error", rs.error_msg)
            while rs.next():
                item = rs.get_row_data()
                sqliteTool.operate_one('insert into profit '
                                       '(code,year,quarter,netProfit,roe,eps,share,yoyEquity) '
                                       'values(?,?,?,?,?,?,?,?)',
                                       (item[0], year, 4, item[6], item[3], item[7], item[9],yoyEquity))
    bs.logout()

    result = profit("sh.603886", 2022, 4)
    print(result)
