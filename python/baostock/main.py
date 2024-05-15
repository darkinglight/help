from tkinter import *
from tkinter import ttk
import baostock as bs
from peg import get_peg, peg_list
from self import self_add, self_alter, self_list_code
from baseinfo import base_info_like


def deploy_menu():
    # 主菜单
    menu = Menu(win)
    win.config(menu=menu)
    # 子菜单-文件
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="股票", menu=filemenu)
    # 文件菜单-菜单项
    filemenu.add_command(label="添加股票", command=add_stock, accelerator="Ctrl-N")
    filemenu.add_command(label="退出", command=win.quit, accelerator="Esc")


def add_stock():
    def calculate():
        bs.login()
        base_info_data = base_info_like(codeValue.get())
        if base_info_data is None:
            return
        data = get_peg(base_info_data.code, "2024-05-08")
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
    tree.delete(*tree.get_children())
    pegs = peg_list()
    # 添加数据到表格
    for item in pegs:
        if item.roeAvg > 0 and item.dividendAvg > 0 and item.peg > 0 and item.assetToEquity < 2:
            tree.insert('', 'end', text=item.code, values=(item.name, item.peg, item.roeAvg, item.dividendAvg))


def show_self():
    tree.delete(*tree.get_children())
    self_stocks = self_list_code()
    pegs = peg_list()
    for item in pegs:
        if item.code in self_stocks:
            tree.insert('', 'end', text=item.code, values=(item.name, item.peg, item.roeAvg, item.dividendAvg))


def tree_click(event):
    selected_node = tree.focus()
    node_text = tree.item(selected_node)["text"]
    self_alter(node_text)


win = Tk()
win.title(string="智能选股")
deploy_menu()

# 第一个窗体
frame1 = Frame(win, relief=RAISED, borderwidth=2)
frame1.pack(side=TOP, fill=BOTH, ipadx=13, ipady=13, expand=0)
Button(frame1, padx=2, pady=2, text="全部", command=show_all).grid(row=0, column=0)
Button(frame1, padx=2, pady=2, text="自选", command=show_self).grid(row=0, column=1)
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
