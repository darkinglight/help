import baostock as bs
import pandas as pd

lg = bs.login()

rs = bs.query_history_k_data_plus("sh.601012", "date,code,close,peTTM,pbMRQ,psTTM,pcfNcfTTM", start_date='2021-01-01',frequency="d", adjustflag="3")

result_list = []
while (rs.error_code == '0') & rs.next():
    result_list.append(rs.get_row_data())
print(result_list[len(result_list) - 1][3])
result = pd.DataFrame(result_list, columns=rs.fields)

result.to_csv("evalue.csv", encoding="utf-8", index=False)
print(result)

bs.logout()
