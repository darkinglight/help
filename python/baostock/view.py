from SqliteTool import SqliteTool

if __name__ == "__main__":
    sqliteTool = SqliteTool()
    list = sqliteTool.query_many("select code,name,roeAvg,yoyEquityAvg,dividendAvg,realGrowth,peg"
                                 " from rating1 "
                                 "where 1 = 1 "
                                 "and peg > 0 and roeAvg < 30 and roeAvg > yoyEquityAvg "
                                 #"and code in ('sh.600566','sz.002088','sz.002884',"
                                 #"'sz.002833','sz.000651') "
                                 "order by peg limit 100")
    for item in list:
        print(item)
        print("\n")

