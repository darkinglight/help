from collections import namedtuple

from SqliteTool import SqliteTool

from allstock import allstock
from baseinfo import baseinfo
import baostock as bs

# code	证券代码
# year	年
# quarter	季度
# CAToAsset	流动资产除以总资产
# NCAToAsset	非流动资产除以总资产
# tangibleAssetToAsset	有形资产除以总资产
# ebitToInterest	已获利息倍数	息税前利润/利息费用
# CFOToOR	经营活动产生的现金流量净额除以营业收入
# CFOToNP	经营性现金净流量除以净利润
Cash = namedtuple("Cash", ['code', 'year', 'quarter', 'CAToAsset', 'NCAToAsset',
                           'tangibleAssetToAsset', 'ebitToInterest', 'CFOToOR', 'CFOToNP'])


def create_table():
    # 创建数据表dividend的SQL语句
    create_tb_sql = ("create table if not exists cash ("
                     "id INTEGER PRIMARY KEY,"
                     "code text,"
                     "year text,"
                     "quarter text,"
                     "CAToAsset float default 0,"
                     "NCAToAsset float default 0,"
                     "tangibleAssetToAsset float default 0,"
                     "ebitToInterest float default 0,"
                     "CFOToOR float default 0,"
                     "CFOToNP float default 0,"
                     "UNIQUE(code, year, quarter)"
                     ");")
    # 创建对象
    sqlite_tool = SqliteTool()
    sqlite_tool.drop_table("drop table cash")
    # 创建数据表
    sqlite_tool.create_table(create_tb_sql)


def refresh_data():
    sqlite_tool = SqliteTool()
    stocks = allstock()
    bs.login()
    for stock in stocks:
        base_data = baseinfo(stock.code)
        if base_data.type != 1:
            continue
        for year in range(2015, 2023):
            if year < int(base_data.ipoDate[0:4]):
                continue
            exist = cash(stock.code, year, 4)
            if exist is not None:
                continue
            rs = bs.query_cash_flow_data(code=stock.code, year=year, quarter=4)
            if rs.error_code != '0':
                print(stock.code, "get cash_flow error", rs.error_msg)
            while rs.next():
                item = rs.get_row_data()
                sqlite_tool.operate_one('insert into cash ('
                                        'code, year, quarter, CAToAsset, NCAToAsset,'
                                        'tangibleAssetToAsset, ebitToInterest, CFOToOR, CFOToNP) '
                                        'values(?,?,?, ?,?,?, ?,?,?)',
                                        (item[0], year, 4, item[3], item[4],
                                         item[5], item[6], item[7], item[8]))
    bs.logout()


def cash(code, year, quarter):
    sqlite_tool = SqliteTool()
    data = sqlite_tool.query_one("select code, year, quarter, CAToAsset, NCAToAsset,"
                                 "tangibleAssetToAsset, ebitToInterest, CFOToOR, CFOToNP"
                                 " from cash where code = :code "
                                 "and year = :year and quarter = :quarter",
                                 {"code": code, "year": year, "quarter": quarter})
    if data is None:
        return data
    dto = Cash(code=data[0], year=data[1], quarter=data[2], CAToAsset=data[3],
               NCAToAsset=data[4], tangibleAssetToAsset=data[5], ebitToInterest=data[6],
               CFOToOR=data[7], CFOToNP=data[8])
    return dto


if __name__ == "__main__":
    create_table()
    refresh_data()
