from SqliteTool import SqliteTool
from baseinfo import baseinfo, base_info_list
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


def refresh_all(date):
    exist_peg = peg_list()
    exist_codes = []
    for peg in exist_peg:
        exist_codes.append(peg.code)
    stocks = base_info_list()
    for stock in stocks:
        if stock.code in exist_codes:
            continue
        get_peg(stock.code, date)
        print("refresh peg ", stock.name)


def get_peg(code, date):
    year = int(date[0:4]) - 1
    quarter = 4

    base = baseinfo(code)
    if int(base.ipoDate[0:4]) >= year - 3:
        return None
    name = base.name

    price_data = priceinfo(code, date)
    if price_data is None:
        return None
    pe = price_data.pe
    pb = price_data.pb

    profit0 = profit(code, year, quarter)
    profit1 = profit(code, year - 1, quarter)
    profit2 = profit(code, year - 2, quarter)
    profit3 = profit(code, year - 3, quarter)
    roeAvg = 0
    yoyEquityAvg = 0
    profileCount = 0
    for profit_item in [profit0, profit1, profit2, profit3]:
        if profit_item is None:
            continue
        roeAvg += profit_item.roe
        yoyEquityAvg += profit_item.yoyEquity
        profileCount += 1
    roeAvg = roeAvg * 100 / profileCount
    yoyEquityAvg = yoyEquityAvg * 100 / profileCount
    dividendAvg = (roeAvg - yoyEquityAvg) / pb
    realGrowth = dividendAvg + yoyEquityAvg
    peg = pe / (dividendAvg * 1.5 + yoyEquityAvg)

    dupont_data = dupont(code, year, quarter)
    if dupont_data is None:
        return None
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


def peg_list():
    select_sql = ("select * from peg "
                  "where roeAvg > 0 and dividendAvg > 0 and peg > 0 and assetToEquity < 3 "
                  "order by peg asc;")
    datas = sqliteTool.query_many(select_sql)
    result = []
    for item in datas:
        peg = Peg(code=item[0],
                  name=item[1],
                  pe=item[2],
                  pb=item[3],
                  roeAvg=item[4],
                  yoyEquityAvg=item[5],
                  dividendAvg=item[6],
                  realGrowth=item[7],
                  peg=item[8],
                  assetToEquity=item[9])
        result.append(peg)
    return result


# peg's pe use peAvg = pb/roeAvg
if __name__ == "__main__":
    # init_table()
    bs.login()
    # print(get_peg("sh.603886", "2024-05-08"))
    refresh_all("2024-05-08")
    bs.logout()
