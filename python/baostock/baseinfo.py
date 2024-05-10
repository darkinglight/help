from collections import namedtuple

import baostock as bs
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
    dto = base_info_from_db(code)
    if dto is None:
        dto = base_info_from_api(code)
    return dto


def base_info_from_db(code):
    sqlite_tool = SqliteTool()
    select_sql = 'select code, name, ipoDate, outDate, type, status from baseinfo where code = :code'
    base_data = sqlite_tool.query_one(select_sql, {"code": code})
    if base_data is None:
        return None
    dto = BaseInfo(code=base_data[0], name=base_data[1], ipoDate=base_data[2],
                   outDate=base_data[3], type=base_data[4], status=base_data[5])
    return dto


def base_info_from_api(code):
    dto = None
    sqliteTool = SqliteTool()
    rs = bs.query_stock_basic(code=code)
    if rs.error_code != '0':
        print("get baseinfo error: ", code, rs.error_code, rs.error_msg)
        return dto
    while rs.next():
        base_data = rs.get_row_data()
        sqliteTool.operate_one('insert into baseinfo values(?,?,?,?,?,?)',
                               (base_data[0], base_data[1], base_data[2],
                                base_data[3], base_data[4], base_data[5]))
        dto = BaseInfo(code=base_data[0], name=base_data[1], ipoDate=base_data[2],
                       outDate=base_data[3], type=base_data[4], status=base_data[5])
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

    data = baseinfo('sh.603886')
    print(data)
