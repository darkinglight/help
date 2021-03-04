import baostock as bs
import pandas as pd
import matplotlib.pyplot as plt

lg = bs.login()

fields = "date,code,open,high,low,close"
rs = bs.query_history_k_data("sh.000001", fields, start_date='2000-01-01', end_date='2018-09-07', frequency="d", adjustflag="2")

data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
result.index = pd.to_datetime(result.date)
result.head()
result.info()

result = result.apply(pd.to_numeric, errors='ignore')
result.info()

result.close.plot(figsize=(16,8))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()
