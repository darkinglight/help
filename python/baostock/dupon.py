from collections import namedtuple

import baostock as bs
import pandas as pd
import os

from SqliteTool import SqliteTool


def init():
    # 创建数据表dividend的SQL语句
    create_tb_sql = ("create table if not exists dupon ("
                     "id INTEGER PRIMARY KEY,"
                     "code text,"
                     "statDate text,"
                     "dupontROE float default 0,"
                     "dupontAssetStoEquity float default 0,"
                     "dupontAssetTurn float default 0,"
                     "dupontPnitoni float default 0,"
                     "dupontNitogr float default 0,"
                     "dupontTaxBurden int default 0,"
                     "dupontIntburden float default 0,"
                     "dupontEbittogr float default 0"
                     ");")
    # 创建对象
    sqliteTool = SqliteTool()
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
        rs_dupont = bs.query_dupont_data(code=stock.code, year=2022, quarter=4)
        while (rs_dupont.error_code == '0') & rs_dupont.next():
            item = rs_dupont.get_row_data()
            sqliteTool.operate_one('insert or replace into dupon '
                                   '(code,statDate,dupontROE,dupontAssetStoEquity,dupontAssetTurn,dupontPnitoni,'
                                   'dupontNitogr,dupontTaxBurden,dupontIntburden,dupontEbittogr) '
                                   'values(?,?,?, ?,?,?, ?,?,?, ?)',
                                   (item[0], item[2], item[3], item[4], item[5], item[6],
                                    item[7], item[8], item[9], item[10]))
    bs.logout()

Dupon = namedtuple("Dupon", ['code','statDate','dupontROE',
                             'dupontAssetStoEquity','dupontAssetTurn','dupontPnitoni',
                                   'dupontNitogr','dupontTaxBurden','dupontIntburden','dupontEbittogr'])
def dupont(code):
    sqliteTool = SqliteTool()
    data = sqliteTool.query_one("select code,statDate,dupontROE,dupontAssetStoEquity,"
                                "dupontAssetTurn,dupontPnitoni,dupontNitogr,"
                                "dupontTaxBurden,dupontIntburden,dupontEbittogr"
                                " from dupon where code = :code",
                                {"code": code})
    if data == None:
        return data
    try:
        assetToEquity = float(data[3])
    except ValueError:
        assetToEquity = 0
    return Dupon(code=data[0],statDate=data[1],dupontROE=data[2],dupontAssetStoEquity=assetToEquity,
                 dupontAssetTurn=data[4],dupontPnitoni=data[5],dupontNitogr=data[6],
                 dupontTaxBurden=data[7],dupontIntburden=data[8],dupontEbittogr=data[9])


if __name__ == "__main__":
    #init()
    print(dupont("sh.600007"))
