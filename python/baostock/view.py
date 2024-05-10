from SqliteTool import SqliteTool

def listAll():
    sqliteTool = SqliteTool()
    list = sqliteTool.query_many("select code,name,roeAvg,realGrowth,peAvg,pegAvg"
                                 " from rating1 "
                                 "where 1 = 1 "
                                 "and peg > 0 "
                                 "and roeAvg < 30 "
                                 "and roeAvg > yoyEquityAvg "
                                 "and dividendAvg > 3 "
                                 "and assetToEquity < 2 "
                                 "order by pegAvg limit 100")
    for item in list:
        print(item)
        print("\n")

def listAllByPb():
    sqliteTool = SqliteTool()
    list = sqliteTool.query_many("select code,name,roeAvg,realGrowth,realGrowth / pb as growthPerPb"
                                 " from rating1 "
                                 "where 1 = 1 "
                                 "and peg > 0 "
                                 "and roeAvg < 30 "
                                 "and roeAvg > yoyEquityAvg "
                                 "and dividendAvg > 3 "
                                 "and assetToEquity < 2 "
                                 "order by growthPerPb desc limit 100")
    for item in list:
        print(item)
        print("\n")

def listSelf():
    sqliteTool = SqliteTool()
    list = sqliteTool.query_many("select code,name,roeAvg,realGrowth,peAvg,pegAvg"
                                 " from rating1 "
                                 "where 1 = 1 "
                                 "and peg > 0 "
                                 # "and roeAvg < 30 "
                                 # "and roeAvg > yoyEquityAvg "
                                 # "and dividendAvg > 3 "
                                 # "and assetToEquity < 3 "
                                 "and code in ("
                                 "'sz.000651',"
                                 "'sz.000848',"
                                 "'sz.000858',"
                                 "'sz.002014',"
                                 "'sz.002088',"
                                 "'sz.002158',"
                                 "'sz.002223',"
                                 "'sz.002318',"
                                 "'sz.002478',"
                                 "'sz.002597',"
                                 "'sz.002727',"
                                 "'sz.002737',"
                                 "'sz.002818',"
                                 "'sz.002833',"
                                 "'sz.002867',"
                                 "'sz.002884',"
                                 "'sh.600210',"
                                 "'sh.600273',"
                                 "'sh.600332',"
                                 "'sh.600511',"
                                 "'sh.600566',"
                                 "'sh.600690',"
                                 "'sh.600741',"
                                 "'sh.601012',"
                                 "'sh.601811',"
                                 "'sh.603279',"
                                 "'sh.603360',"
                                 "'sh.603365',"
                                 "'sh.603611',"
                                 "'sh.603757',"
                                 "'sh.603886'"
                                 ") "
                                 "order by pegAvg limit 100")
    for item in list:
        print(item)
        print("\n")


def listSelfByPb():
    sqliteTool = SqliteTool()
    list = sqliteTool.query_many("select code,name,roeAvg,realGrowth,realGrowth / pb as growthPerPb"
                                 " from rating1 "
                                 "where 1 = 1 "
                                 "and peg > 0 "
                                 "and roeAvg < 30 "
                                 "and roeAvg > yoyEquityAvg "
                                 "and dividendAvg > 3 "
                                 "and assetToEquity < 2 "
                                 "and code in ("
                                 "'sz.000651',"
                                 "'sz.000848',"
                                 "'sz.000858',"
                                 "'sz.002014',"
                                 "'sz.002088',"
                                 "'sz.002158',"
                                 "'sz.002223',"
                                 "'sz.002318',"
                                 "'sz.002478',"
                                 "'sz.002597',"
                                 "'sz.002727',"
                                 "'sz.002737',"
                                 "'sz.002818',"
                                 "'sz.002833',"
                                 "'sz.002867',"
                                 "'sz.002884',"
                                 "'sh.600210',"
                                 "'sh.600273',"
                                 "'sh.600332',"
                                 "'sh.600511',"
                                 "'sh.600566',"
                                 "'sh.600690',"
                                 "'sh.600741',"
                                 "'sh.601012',"
                                 "'sh.601811',"
                                 "'sh.603279',"
                                 "'sh.603360',"
                                 "'sh.603365',"
                                 "'sh.603611',"
                                 "'sh.603757',"
                                 "'sh.603886'"
                                 ") "
                                 "order by growthPerPb desc limit 100")
    for item in list:
        print(item)
        print("\n")

def getDetail(code):
    sqliteTool = SqliteTool()
    result = sqliteTool.query_one("select * from rating1 where code = :code", {"code": code})
    print(result)


if __name__ == "__main__":
    listAll()
    # listAllByPb()
    # listSelf()
    # listSelfByPb()
    #getDetail("sz.002478")
