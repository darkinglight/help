# -*- coding: utf-8 -*-
import baostock as bs
import pandas as pd
from SqliteTool import SqliteTool


def dividend(code):
    sqlite_tool = SqliteTool()
    select_sql = "select code from dividend where code = :code;"
    result = sqlite_tool.query_one(select_sql, {"code": code})
    return result


if __name__ == "__main__":
    # 创建数据表dividend的SQL语句
    create_tb_sql = ("create table if not exists dividend ("
                     "id INTEGER PRIMARY KEY,"
                     "code text,"
                     "payDate text,"
                     "cashPsBeforeTax float default 0,"
                     "cashPsAfterTax float default 0,"
                     "stocksPs float default 0,"
                     "cashStock text,"
                     "reserveToStockPs float default 0,"
                     "UNIQUE(code, payDate)"
                     ");")
    # 创建对象
    sqliteTool = SqliteTool()
    sqliteTool.drop_table("drop table dividend")
    # 创建数据表
    sqliteTool.create_table(create_tb_sql)

    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    code = "sh.603886"
    for year in range(2020, 2023):
        rs = bs.query_dividend_data(code=code, year=year, yearType="report")
        if rs.error_code != '0':
            print(code, "get dividend error", rs.error_msg)
        while rs.next():
            item = rs.get_row_data()
            print(item)
            sqliteTool.operate_one('insert into dividend '
                                   '(code,payDate,cashPsBeforeTax,cashPsAfterTax,'
                                   'stocksPs,cashStock,reserveToStockPs) '
                                   'values(?,?,?,?,?,?,?)',
                                   (item[0], item[7], item[9], item[10], item[11], item[12], item[13]))
    bs.logout()
