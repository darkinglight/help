import tkinter
from baseinfo import baseinfo


def calculate():
    data = baseinfo(codeValue.get())
    message = "code:\t" + data.code + "\n" + "name:\t" + data.name
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
