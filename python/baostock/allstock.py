import baostock as bs
import pandas as pd
import os
from SqliteTool import SqliteTool


def allstock():
    result = []
    return result


if __name__ == "__main__":
    # 创建数据表info的SQL语句
    create_tb_sql = ("create table if not exists stock("
                     "code text primary key,"
                     "status int not null,"
                     "name text);")
    # 创建对象
    sqliteTool = SqliteTool()
    # 创建数据表
    sqliteTool.create_table(create_tb_sql)

    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:' + lg.error_code)
    print('login respond  error_msg:' + lg.error_msg)

    rs = bs.query_all_stock(day="2023-01-01")
    print('query_all_stock respond error_code:' + rs.error_code)
    print('query_all_stock respond  error_msg:' + rs.error_msg)
    while (rs.error_code == '0') & rs.next():
        item = rs.get_row_data()
        sqliteTool.operate_one('insert into stock values(?,?,?)',
                               (item['code'], item['tradeStatus'], item['code_name']))
    bs.logout()

    # 查询数据
    select_sql = "select * from stock;"
    result_many = sqliteTool.query_many(select_sql)
    print(result_many)
