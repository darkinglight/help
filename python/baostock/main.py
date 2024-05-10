import tkinter
import baostock as bs
from peg import get_peg


def calculate():
    bs.login()
    data = get_peg(codeValue.get(), "2024-05-08")
    bs.logout()

    message = "code:\t" + data.code + "\n"
    message += "name:\t" + data.name + "\n"
    message += "pe:\t" + str(data.pe) + "\n"
    message += "pb:\t" + str(data.pb) + "\n"
    message += "roeAvg:\t" + str(data.roeAvg) + "\n"
    message += "增长率:\t" + str(data.yoyEquityAvg) + "\n"
    message += "股息率:\t" + str(data.dividendAvg) + "\n"
    message += "回报率:\t" + str(data.realGrowth) + "\n"
    message += "股息*1.5peg:\t" + str(data.peg) + "\n"
    message += "总资产/净资产:\t" + str(data.assetToEquity) + "\n"

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
