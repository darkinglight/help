from SqliteTool import SqliteTool
from baseinfo import baseinfo
from profit import profit
from dupon import dupont
from priceinfo import priceinfo
import baostock as bs
from collections import namedtuple

sqliteTool = SqliteTool()

Peg = namedtuple("Peg", [
    "code",
    "name",
    "pe",
    "pb",
    "roeAvg",
    "yoyEquityAvg",
    "dividendAvg",
    "realGrowth",
    "peg",
    "assetToEquity"
])


def init_table():
    create_tb_sql = ("create table if not exists peg ("
                     "code text PRIMARY KEY,"
                     "name text,"
                     "pe float default 0,"
                     "pb float default 0,"
                     "roeAvg float default 0,"
                     "yoyEquityAvg float default 0,"
                     "dividendAvg float default 0,"
                     "realGrowth float default 0,"
                     "peg float default 0,"
                     "assetToEquity float default 0"
                     ");")
    # 创建对象
    sqliteTool.drop_table("drop table peg")
    # 创建数据表
    sqliteTool.create_table(create_tb_sql)


def get_peg(code, date):
    year = int(date[0:4]) - 1
    quarter = 4

    base = baseinfo(code)
    if int(base.ipoDate[0:4]) >= year - 3:
        return None
    name = base.name

    price_data = priceinfo(code, date)
    pe = price_data.pe
    pb = price_data.pb

    profit0 = profit(code, year, quarter)
    profit1 = profit(code, year - 1, quarter)
    profit2 = profit(code, year - 2, quarter)
    profit3 = profit(code, year - 3, quarter)
    if profit0 is None:
        return None
    roeAvg = (profit0.roe + profit1.roe + profit2.roe + profit3.roe) * 100 / 4
    yoyEquityAvg = (profit0.yoyEquity + profit1.yoyEquity + profit2.yoyEquity +
                    profit3.yoyEquity) * 100 / 4
    dividendAvg = (roeAvg - yoyEquityAvg) / pb
    realGrowth = dividendAvg + yoyEquityAvg
    peg = pe / (dividendAvg * 1.5 + yoyEquityAvg)

    dupont_data = dupont(code, year, quarter)
    asset_to_equity = dupont_data.dupontAssetStoEquity

    sqliteTool.operate_one('insert or replace into peg '
                           '(code, name, pe, pb, roeAvg, yoyEquityAvg,'
                           'dividendAvg,realGrowth,peg,assetToEquity) '
                           'values(?,?,?, ?,?,?, ?,?,?,?) ',
                           (code, name, pe, pb, roeAvg, yoyEquityAvg,
                            dividendAvg, realGrowth, peg, asset_to_equity))

    return Peg(code=code,
               name=name,
               pe=pe,
               pb=pb,
               roeAvg=roeAvg,
               yoyEquityAvg=yoyEquityAvg,
               dividendAvg=dividendAvg,
               realGrowth=realGrowth,
               peg=peg,
               assetToEquity=asset_to_equity)


# peg's pe use peAvg = pb/roeAvg
if __name__ == "__main__":
    init_table()
    bs.login()
    print(get_peg("sh.603886", "2024-05-08"))
    bs.logout()
