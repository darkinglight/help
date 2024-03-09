# -*- coding: utf-8 -*-
from dataclasses import dataclass

import baostock as bs
from SqliteTool import SqliteTool
from allstock import allstock
from baseinfo import baseinfo


@dataclass
class Dividend:
    code: str  # 股票代码
    dividPreNoticeDate: str  # 预批露公告日
    dividAgmPumDate: str  # 股东大会公告日期
    dividPlanAnnounceDate: str  # 预案公告日
    dividPlanDate: str  # 分红实施公告日
    dividRegistDate: str  # 股权登记告日
    dividOperateDate: str  # 除权除息日期
    dividPayDate: str  # 派息日
    dividStockMarketDate: str  # 红股上市交易日
    dividCashPsBeforeTax: float  # 每股股利税前	派息比例分子(税前)/派息比例分母
    dividCashPsAfterTax: str  # 每股股利税后	派息比例分子(税后)/派息比例分母
    dividStocksPs: float  # 每股红股
    dividCashStock: str  # 分红送转	每股派息数(税前)+每股送股数+每股转增股本数
    dividReserveToStockPs: float  # 每股转增资本


def dividend(code):
    sqlite_tool = SqliteTool()
    select_sql = "select code from dividend where code = :code;"
    data = sqlite_tool.query_one(select_sql, {"code": code})
    return data


def init():
    # 创建数据表dividend的SQL语句
    create_tb_sql = ("create table if not exists dividend ("
                     "id INTEGER PRIMARY KEY,"
                     "code text,"
                     "dividPreNoticeDate text,"
                     "dividAgmPumDate text,"
                     "dividPlanAnnounceDate text,"
                     "dividPlanDate text,"
                     "dividRegistDate text,"
                     "dividOperateDate text,"
                     "dividPayDate text,"
                     "dividStockMarketDate text,"
                     "dividCashPsBeforeTax float default 0,"
                     "dividCashPsAfterTax float default 0,"
                     "dividStocksPs float default 0,"
                     "dividCashStock float default 0,"
                     "dividReserveToStockPs float default 0,"
                     "UNIQUE(code, dividPayDate)"
                     ");")
    # 创建对象
    sqlite_tool = SqliteTool()
    sqlite_tool.drop_table("drop table dividend")
    # 创建数据表
    sqlite_tool.create_table(create_tb_sql)


def get_data(code, year):
    rs = bs.query_dividend_data(code=code, year=year, yearType="report")
    if rs.error_code != '0':
        print(code, "get dividend error", rs.error_msg)
    datas = []
    while rs.next():
        item = rs.get_row_data()
        dto = Dividend(item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7],
                       item[8], item[9], item[10], item[11], item[12], item[13])
        datas.append(dto)
    return datas


def refresh():
    sqlite_tool = SqliteTool()
    stocks = allstock()
    for stock in stocks:
        base_data = baseinfo(stock.code)
        if base_data.type != 1:
            continue
        for year in range(2020, 2024):
            datas = get_data(stock.code, year)
            for item in datas:
                sqlite_tool.operate_one('insert into dividend ('
                                        'code,'
                                        'dividPreNoticeDate,'
                                        'dividAgmPumDate,'
                                        'dividPlanAnnounceDate,'
                                        'dividPlanDate,'
                                        'dividRegistDate,'
                                        'dividOperateDate,'
                                        'dividPayDate,'
                                        'dividStockMarketDate,'
                                        'dividCashPsBeforeTax,'
                                        'dividCashPsAfterTax,'
                                        'dividStocksPs,'
                                        'dividCashStock,'
                                        'dividReserveToStockPs'
                                        ') values(?,?,?, ?,?,?, ?,?,?, ?,?,?, ?,?)',
                                        (item.code,
                                         item.dividPreNoticeDate,
                                         item.dividAgmPumDate,
                                         item.dividPlanAnnounceDate,
                                         item.dividPlanDate,
                                         item.dividRegistDate,
                                         item.dividOperateDate,
                                         item.dividPayDate,
                                         item.dividStockMarketDate,
                                         item.dividCashPsBeforeTax,
                                         item.dividCashPsAfterTax,
                                         item.dividStocksPs,
                                         item.dividCashStock,
                                         item.dividReserveToStockPs))


if __name__ == "__main__":
    bs.login()
    # result = get_data("sh.603886", 2022)
    # print(result)

    init()
    refresh()
    bs.logout()
