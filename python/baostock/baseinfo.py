import baostock as bs
import pandas as pd

lg = bs.login()
rs = bs.query_stock_basic(code="sh.601012")

data_list = []
while(rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
print(data_list[0][2])
print(result)

bs.logout()
