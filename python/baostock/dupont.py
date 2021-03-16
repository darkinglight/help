import baostock as bs
import pandas as pd

lg = bs.login()

code = "sh.601012"
year = 2020
quarter = 3
dupont_list = []
rs_dupont = bs.query_dupont_data(code=code, year=year, quarter=quarter)
while (rs_dupont.error_code == '0') & rs_dupont.next():
    dupont_list.append(rs_dupont.get_row_data())
result_profile = pd.DataFrame(dupont_list, columns=rs_dupont.fields)

result_profile.to_csv("data/dupont_{}_{}_{}.csv".format(code,year,quarter), encoding="utf-8", index=False)

bs.logout()
