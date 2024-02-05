from SqliteTool import SqliteTool

if __name__ == "__main__":
    sqliteTool = SqliteTool()
    list = sqliteTool.query_many("select code,name,roeAvg,yoyEquityAvg,dividendAvg,realGrowth,peg"
                                 " from rating1 "
                                 "where 1 = 1 "
                                 "and peg > 0 "
                                 #"and roeAvg < 30 "
                                 #"and roeAvg > yoyEquityAvg "
                                 "and dividendAvg > 5 "
                                 "and assetToEquity < 2 "
                                # "and code in ('sh.600566','sz.002088','sz.002884',"
                                # "'sz.002833','sz.000651','sh.601012','sh.603611',"
                                # "'sz.002597','sz.002737','sh.600511','sh.600332',"
                                # "'sz.002318','sz.000848','sz.000858','sh.603886',"
                                # "'sh.603365','sz.002867','sz.002818','sh.601811',"
                                # "'sz.002014','sh.603279','sh.600690') "
                                 "order by peg limit 100")
    for item in list:
        print(item)
        print("\n")

