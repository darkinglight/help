import baostock as bs
import pandas as pd
import os

def dupont(code, year, quarter):
    filename = "data/dupont_{}_{}_{}.csv".format(code,year,quarter)
    
    if os.path.exists(filename):
        # get from local
        result_profile = pd.read_csv(filename)
    else:
        # get from remote
        dupont_list = []
        rs_dupont = bs.query_dupont_data(code=code, year=year, quarter=quarter)
        while (rs_dupont.error_code == '0') & rs_dupont.next():
            dupont_list._append(rs_dupont.get_row_data())
        result_profile = pd.DataFrame(dupont_list, columns=rs_dupont.fields)
        result_profile.to_csv(filename, encoding="utf-8", index=False)
    return result_profile


