import tkinter
from baseinfo import baseinfo
from profit import profit
from priceinfo import priceinfo


def calculate():
    data = baseinfo(codeValue.get())
    message = "code:\t" + data.code + "\n"
    message += "name:\t" + data.name + "\n"

    price_data = priceinfo(codeValue.get(), "2024-05-08")
    message += "pe:\t" + str(price_data.pe) + "\n"
    message += "pb:\t" + str(price_data.pb) + "\n"

    profit_data2023 = profit(codeValue.get(), 2023, 4)
    profit_data2022 = profit(codeValue.get(), 2022, 4)
    profit_data2021 = profit(codeValue.get(), 2021, 4)
    profit_data2020 = profit(codeValue.get(), 2020, 4)
    roeAvg = (profit_data2020.roe + profit_data2021.roe + profit_data2022.roe + profit_data2023.roe) * 100 / 4
    yoyEquityAvg = (profit_data2020.yoyEquity + profit_data2021.yoyEquity + profit_data2022.yoyEquity +
                    profit_data2023.yoyEquity) * 100 / 4
    dividendAvg = (roeAvg - yoyEquityAvg) / price_data.pb

    growth = dividendAvg + yoyEquityAvg
    peg = price_data.pe / growth
    peg2 = price_data.pe / (dividendAvg * 1.5 + yoyEquityAvg)

    message += "roeAvg:\t" + str(roeAvg) + "\n"
    message += "增长率:\t" + str(yoyEquityAvg) + "\n"
    message += "股息率:\t" + str(dividendAvg) + "\n"
    message += "回报率:\t" + str(growth) + "\n"
    message += "peg:\t" + str(peg) + "\n"
    message += "股息*1.5peg:\t" + str(peg2) + "\n"

    result.config(text=message)


win = tkinter.Tk()
win.title(string="智能选股")

tkinter.Label(win, text="股票代码:", font=("微软雅黑", 14)).grid(row=0, column=0)
codeValue = tkinter.StringVar()
codeValue.set("sh.603886")
tkinter.Entry(win, textvariable=codeValue).grid(row=0, column=1)

tkinter.Button(win, padx=2, pady=2, text="估值", command=calculate).grid(row=1, column=1)

result = tkinter.Label(win, text="", font=("微软雅黑", 14))
result.grid(row=2, column=0)

win.mainloop()
