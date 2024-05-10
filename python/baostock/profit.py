from collections import namedtuple
from SqliteTool import SqliteTool
import baostock as bs

# roeAvg	净资产收益率(平均)(%)	归属母公司股东净利润/[(期初归属母公司股东的权益+期末归属母公司股东的权益)/2]*100%
# npMargin	销售净利率(%)	净利润/营业收入*100%
# gpMargin	销售毛利率(%)	毛利/营业收入*100%=(营业收入-营业成本)/营业收入*100%
# netProfit	净利润(元)
# epsTTM	每股收益	归属母公司股东的净利润TTM/最新总股本
# MBRevenue	主营营业收入(元)
# totalShare	总股本
# YOYEquity	净资产同比增长率	(本期净资产-上年同期净资产)/上年同期净资产的绝对值*100%
Profit = namedtuple("Profit", ['code', 'year', 'quarter',
                               'netProfit', 'roe', 'eps', 'share', 'yoyEquity'])


def profit(code, year, quarter):
    dto = profit_from_db(code, year, quarter)
    if dto is None:
        dto = profit_from_api(code, year, quarter)
    return dto


def profit_from_db(code, year, quarter):
    sqliteTool = SqliteTool()
    data = sqliteTool.query_one("select code,year,quarter,netProfit,"
                                "roe,eps,share,yoyEquity"
                                " from profit where code = :code "
                                "and year = :year and quarter = :quarter",
                                {"code": code, "year": year, "quarter": quarter})
    if data == None:
        return data
    try:
        roeData = float(data[4])
    except ValueError:
        roeData = 0
    try:
        yoyEquityData = float(data[7])
    except ValueError:
        yoyEquityData = 0
    dto = Profit(code=data[0], year=data[1], quarter=data[2], netProfit=data[3],
                 roe=roeData, eps=data[5], share=data[6], yoyEquity=yoyEquityData)
    return dto


def profit_from_api(code, year, quarter):
    dto = None
    yoyEquity = 0
    rs = bs.query_growth_data(code=code, year=year, quarter=quarter)
    if rs.error_code != '0':
        print(code, "get growth error", rs.error_msg)
    while rs.next():
        item = rs.get_row_data()
        yoyEquity = item[3]
    rs = bs.query_profit_data(code=code, year=year, quarter=quarter)
    if rs.error_code != '0':
        print(code, "get profit error", rs.error_msg)
        return dto
    sqliteTool = SqliteTool()
    while rs.next():
        item = rs.get_row_data()
        sqliteTool.operate_one('insert into profit '
                               '(code,year,quarter,netProfit,roe,eps,share,yoyEquity) '
                               'values(?,?,?,?,?,?,?,?)',
                               (item[0], year, quarter, item[6], item[3], item[7], item[9], yoyEquity))
        dto = Profit(code=item[0], year=year, quarter=quarter, netProfit=item[6],
                     roe=item[3], eps=item[7], share=item[9], yoyEquity=yoyEquity)
    return dto


if __name__ == "__main__":
    # 创建数据表dividend的SQL语句
    # create_tb_sql = ("create table if not exists profit ("
    #                  "id INTEGER PRIMARY KEY,"
    #                  "code text,"
    #                  "year int,"
    #                  "quarter int,"
    #                  "netProfit float default 0,"
    #                  "roe float default 0,"
    #                  "eps float default 0,"
    #                  "share int default 0,"
    #                  "yoyEquity float default 0,"
    #                  "UNIQUE(code, year, quarter)"
    #                  ");")
    # # 创建对象
    # sqliteTool = SqliteTool()
    # sqliteTool.drop_table("drop table profit")
    # # 创建数据表
    # sqliteTool.create_table(create_tb_sql)
    #
    # stocks = allstock()
    # bs.login()
    # for stock in stocks:
    #     base_data = baseinfo(stock.code)
    #     if base_data.type != 1:
    #         continue
    #     for year in range(2019, 2023):
    #         if year < int(base_data.ipoDate[0:4]):
    #             continue
    #         exist = profit(stock.code, year, 4)
    #         if exist is not None:
    #             continue
    #         yoyEquity = 0
    #         rs = bs.query_growth_data(code=stock.code, year=year, quarter=4)
    #         if rs.error_code != '0':
    #             print(stock.code, "get growth error", rs.error_msg)
    #         while rs.next():
    #             item = rs.get_row_data()
    #             yoyEquity = item[3]
    #         rs = bs.query_profit_data(code=stock.code, year=year, quarter=4)
    #         if rs.error_code != '0':
    #             print(stock.code, "get profit error", rs.error_msg)
    #         while rs.next():
    #             item = rs.get_row_data()
    #             sqliteTool.operate_one('insert into profit '
    #                                    '(code,year,quarter,netProfit,roe,eps,share,yoyEquity) '
    #                                    'values(?,?,?,?,?,?,?,?)',
    #                                    (item[0], year, 4, item[6], item[3], item[7], item[9], yoyEquity))
    # bs.logout()

    result = profit("sh.601939", 2023, 4)
    print(result)
