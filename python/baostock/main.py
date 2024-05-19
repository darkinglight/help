from tkinter import *
from tkinter import ttk
import baostock as bs
from peg import get_peg, peg_list, refresh_all
from self import self_add, self_alter, self_list_code
from baseinfo import base_info_like
from config import get_config, set_config


def deploy_menu():
    # 主菜单
    menu = Menu(win)
    win.config(menu=menu)
    # 子菜单-文件
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="股票", menu=filemenu)
    # 文件菜单-菜单项
    filemenu.add_command(label="添加股票", command=add_stock, accelerator="Ctrl-N")
    filemenu.add_command(label="刷新股票", command=refresh_stock, accelerator="Ctrl-F")
    filemenu.add_command(label="退出", command=win.quit, accelerator="Esc")


def refresh_stock():
    refresh_all("2024-05-17")


def add_stock():
    def calculate():
        bs.login()
        base_info_data = base_info_like(codeValue.get())
        if base_info_data is None:
            return
        data = get_peg(base_info_data.code, dateValue.get())
        self_add(data.code, data.name)
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

    sub_win = Toplevel(master=win)
    sub_win.title("新增股票")
    # 第一个窗体
    frame1 = Frame(sub_win, relief=RAISED, borderwidth=2)
    frame1.pack(side=TOP, fill=BOTH, ipadx=13, ipady=13, expand=0)

    Label(frame1, text="股票代码:", font=("微软雅黑", 14)).grid(row=0, column=0)
    codeValue = StringVar()
    codeValue.set("sh.603886")
    Entry(frame1, textvariable=codeValue).grid(row=0, column=1)

    Label(frame1, text="日期:", font=("微软雅黑", 14)).grid(row=0, column=2)
    dateValue = StringVar()
    dateValue.set("2024-05-09")
    Entry(frame1, textvariable=dateValue).grid(row=0, column=3)

    Button(frame1, padx=2, pady=2, text="估值", command=calculate).grid(row=0, column=4)
    # 第二个窗体
    frame2 = Frame(sub_win, relief=RAISED, borderwidth=2)
    frame2.pack(side=LEFT, fill=X, ipadx="0.1i", ipady="0.1i", expand=1)
    result = Label(frame2, text="", font=("微软雅黑", 14))
    result.grid(row=0, column=0)


def show_all():
    set_config(roeMin.get(), roeMax.get(), dividendMin.get(), dividendMax.get(), assetToEquityMax.get(), self.get())
    tree.delete(*tree.get_children())
    self_stocks = self_list_code()
    pegs = peg_list()
    # 添加数据到表格
    for item in pegs:
        if roeMin is not None and item.roeAvg < roeMin.get():
            continue
        if roeMax is not None and item.roeAvg > roeMax.get():
            continue
        if dividendMin is not None and item.dividendAvg < dividendMin.get():
            continue
        if dividendMax is not None and item.dividendAvg > dividendMax.get():
            continue
        if assetToEquityMax is not None and item.assetToEquity > assetToEquityMax.get():
            continue
        if self.get() is True and item.code not in self_stocks:
            continue
        tree.insert('', 'end', text=item.code,
                    values=(item.name, item.peg, item.roeAvg, item.dividendAvg))


def tree_click(event):
    selected_node = tree.focus()
    node_text = tree.item(selected_node)["text"]
    self_alter(node_text)


win = Tk()
win.title(string="智能选股")
deploy_menu()

config = get_config()

# 第一个窗体
frame1 = Frame(win, relief=RAISED, borderwidth=2)
frame1.pack(side=TOP, fill=BOTH, ipadx=13, ipady=13, expand=0)

Label(frame1, text="roe:", font=("微软雅黑", 14)).grid(row=0, column=0)
roeMin = DoubleVar()
roeMin.set(config.roeMin)
Entry(frame1, textvariable=roeMin).grid(row=0, column=1)
Label(frame1, text="--", font=("微软雅黑", 14)).grid(row=0, column=2)
roeMax = DoubleVar()
roeMax.set(config.roeMax)
Entry(frame1, textvariable=roeMax).grid(row=0, column=3)

Label(frame1, text="股息率:", font=("微软雅黑", 14)).grid(row=1, column=0)
dividendMin = DoubleVar()
dividendMin.set(config.dividendMin)
Entry(frame1, textvariable=dividendMin).grid(row=1, column=1)
Label(frame1, text="--", font=("微软雅黑", 14)).grid(row=1, column=2)
dividendMax = DoubleVar()
dividendMax.set(config.dividendMax)
Entry(frame1, textvariable=dividendMax).grid(row=1, column=3)

Label(frame1, text="总资产/净资产 Max:", font=("微软雅黑", 14)).grid(row=2, column=0)
assetToEquityMax = DoubleVar()
assetToEquityMax.set(config.assetToEquityMax)
Entry(frame1, textvariable=assetToEquityMax).grid(row=2, column=1)

Label(frame1, text="自选股:", font=("微软雅黑", 14)).grid(row=3, column=0)
self = BooleanVar()
self.set(config.self)
Radiobutton(frame1, text="是", value=True, variable=self).grid(row=3, column=1)
Radiobutton(frame1, text="否", value=False, variable=self).grid(row=3, column=2)

Button(frame1, padx=2, pady=2, text="搜索", command=show_all).grid(row=4, column=0)

# 第二个窗体
frame2 = Frame(win, relief=RAISED, borderwidth=2)
frame2.pack(side=LEFT, fill=X, ipadx="0.1i", ipady="0.1i", expand=1)
tree = ttk.Treeview(frame2, columns=('name', 'peg', 'roe', 'dividend'))
tree.pack(fill=BOTH, expand=True)
tree.bind("<Double-Button-1>", tree_click)
# 设置列的标题
for column in ('name', 'peg', 'roe', 'dividend'):
    tree.heading(column, text=column)
# 可以调整列的宽度
tree.column('name', width=100)
tree.column('peg', width=100)

show_all()
win.mainloop()
