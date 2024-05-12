from collections import namedtuple

import baostock as bs
from SqliteTool import SqliteTool
from allstock import allstock

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

sqliteTool = SqliteTool()


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


def base_info_list():
    select_sql = ("select code, name, ipoDate, outDate, type, status from baseinfo "
                  "where type = 1 and status = 1;")
    datas = sqliteTool.query_many(select_sql)
    result = []
    for item in datas:
        stock = BaseInfo(code=item[0], name=item[1], ipoDate=item[2],
                         outDate=item[3], type=item[4], status=item[5])
        result.append(stock)
    return result


def init_baseinfo_table():
    # 创建数据表info的SQL语句
    create_tb_sql = ("create table if not exists baseinfo ("
                     "code text primary key,"
                     "name text,"
                     "ipoDate text,"
                     "outDate text default '3000-01-01',"
                     "type int not null,"
                     "status int not null"
                     ");")
    # 创建对象
    sqliteTool = SqliteTool()
    # 创建数据表
    sqliteTool.drop_table("drop table baseinfo;")
    sqliteTool.create_table(create_tb_sql)


def init_baseinfo():
    exist_baseinfo = base_info_list()
    exist_code = []
    for baseinfo in exist_baseinfo:
        exist_code.append(baseinfo.code)

    stocks = allstock()
    for stock in stocks:
        if stock.code in exist_code:
            continue
        base_info_from_api(stock.code)
        print(stock.code, stock.name)


if __name__ == "__main__":
    # init_baseinfo_table()
    bs.login()
    init_baseinfo()
    # data = baseinfo('sh.600290')
    # print(data)
    bs.logout()
    # print(base_info_list())
