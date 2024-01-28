from collections import namedtuple

import baostock as bs
import pandas as pd
import os
from SqliteTool import SqliteTool

# code	证券代码
# code_name	证券名称
# ipoDate	上市日期
# outDate	退市日期
# type	证券类型，其中1：股票，2：指数，3：其它，4：可转债，5：ETF
# status	上市状态，其中1：上市，0：退市
BaseInfo = namedtuple("BaseInfo",
                      ['code',
                       'name',
                       'ipoDate',
                       'outDate',
                       'type',
                       'status'])

def baseinfo(code):
    sqlite_tool = SqliteTool()
    select_sql = 'select code, name, ipoDate, outDate, type, status from baseinfo where code = :code'
    data = sqlite_tool.query_one(select_sql, {"code": code})
    dto = BaseInfo(code=data[0],name=data[1],ipoDate=data[2],outDate=data[3],type=data[4],status=data[5])
    return dto


if __name__ == "__main__":
    # # 创建数据表info的SQL语句
    # create_tb_sql = ("create table if not exists baseinfo ("
    #                  "code text primary key,"
    #                  "name text,"
    #                  "ipoDate text,"
    #                  "outDate text default '3000-01-01',"
    #                  "type int not null,"
    #                  "status int not null"
    #                  ");")
    # # 创建对象
    # sqliteTool = SqliteTool()
    # # 创建数据表
    # sqliteTool.drop_table("drop table baseinfo;")
    # sqliteTool.create_table(create_tb_sql)
    #
    # from allstock import allstock
    # stocks = allstock()
    # bs.login()
    # for stock in stocks:
    #     rs = bs.query_stock_basic(code=stock.code)
    #     if rs.error_code != '0':
    #         print(stock.code, stock.name, rs.error_code, rs.error_msg)
    #         continue
    #     while rs.next():
    #         item = rs.get_row_data()
    #         print(item)
    #         sqliteTool.operate_one('insert into baseinfo values(?,?,?,?,?,?)',
    #                                (item[0],item[1],item[2],item[3],item[4],item[5]))
    # bs.logout()

    data = baseinfo('sh.603886')
    print(data)
