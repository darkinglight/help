from collections import namedtuple

import baostock as bs

from SqliteTool import SqliteTool

# dupontROE	净资产收益率	归属母公司股东净利润/[(期初归属母公司股东的权益+期末归属母公司股东的权益)/2]*100%
# dupontAssetStoEquity	权益乘数，反映企业财务杠杆效应强弱和财务风险	平均总资产/平均归属于母公司的股东权益
# dupontAssetTurn	总资产周转率，反映企业资产管理效率的指标	营业总收入/[(期初资产总额+期末资产总额)/2]
# dupontPnitoni	归属母公司股东的净利润/净利润，反映母公司控股子公司百分比。如果企业追加投资，扩大持股比例，则本指标会增加。
# dupontNitogr	净利润/营业总收入，反映企业销售获利率
# dupontTaxBurden	净利润/利润总额，反映企业税负水平，该比值高则税负较低。净利润/利润总额=1-所得税/利润总额
# dupontIntburden	利润总额/息税前利润，反映企业利息负担，该比值高则税负较低。利润总额/息税前利润=1-利息费用/息税前利润
# dupontEbittogr	息税前利润/营业总收入，反映企业经营利润率，是企业经营获得的可供全体投资人（股东和债权人）分配的盈利占企业全部营收收入的百分比
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
    sqliteTool.drop_table("drop table dupon;")
    sqliteTool.create_table(create_tb_sql)

    from allstock import allstock
    from baseinfo import baseinfo

    stocks = allstock()
    bs.login()
    for stock in stocks:
        base_data = baseinfo(stock.code)
        if base_data.type != 1:
            continue
        rs_dupont = bs.query_dupont_data(code=stock.code, year=2023, quarter=4)
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

def dupont(code, year, quarter):
    result = dupont_from_db(code, year, quarter)
    if result is None:
        result = dupont_from_api(code, year, quarter)
    return result

def dupont_from_db(code, year, quarter):
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

def dupont_from_api(code, year, quarter):
    rs_dupont = bs.query_dupont_data(code=code, year=year, quarter=quarter)
    result = None
    while (rs_dupont.error_code == '0') & rs_dupont.next():
        item = rs_dupont.get_row_data()
        sqliteTool = SqliteTool()
        sqliteTool.operate_one('insert or replace into dupon '
                               '(code,statDate,dupontROE,dupontAssetStoEquity,dupontAssetTurn,dupontPnitoni,'
                               'dupontNitogr,dupontTaxBurden,dupontIntburden,dupontEbittogr) '
                               'values(?,?,?, ?,?,?, ?,?,?, ?)',
                               (item[0], item[2], item[3], item[4], item[5], item[6],
                                item[7], item[8], item[9], item[10]))
        result = Dupon(code=item[0],statDate=item[2],dupontROE=item[3],dupontAssetStoEquity=item[4],
                 dupontAssetTurn=item[5],dupontPnitoni=item[6],dupontNitogr=item[7],
                 dupontTaxBurden=item[8],dupontIntburden=item[9],dupontEbittogr=item[10])
    return result


if __name__ == "__main__":
    # init()
    bs.login()
    print(dupont("sh.600007", 2024, 4))
    bs.logout()
