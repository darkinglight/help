from collections import namedtuple

from SqliteTool import SqliteTool

sqlite_tool = SqliteTool()

Config = namedtuple("Config", ['id', 'name', 'roeMin', 'roeMax',
                               'dividendMin', 'dividendMax', 'assetToEquityMax', 'self'])


def create_table():
    # 创建数据表dividend的SQL语句
    create_tb_sql = ("create table if not exists config ("
                     "id INTEGER PRIMARY KEY,"
                     "name text,"
                     "roeMin float default 0,"
                     "roeMax float default 0,"
                     "dividendMin float default 0,"
                     "dividendMax float default 0,"
                     "assetToEquityMax float default 0,"
                     "self boolean default false,"
                     "status integer default 0"
                     ");")
    # 创建对象
    sqlite_tool.drop_table("drop table if exists config")
    # 创建数据表
    sqlite_tool.create_table(create_tb_sql)


def get_configs():
    datas = sqlite_tool.query_many("select * from config")
    result = []
    for data in datas:
        item = transfer(data)
        result.append(item)
    return result


def get_config():
    name = "default"
    data = sqlite_tool.query_one("select * from config where name = :name", {"name": name})
    if data is None:
        return None
    return transfer(data)


def transfer(data):
    return Config(id=data[0], name=data[1], roeMin=data[2], roeMax=data[3], dividendMin=data[4],
                  dividendMax=data[5], assetToEquityMax=data[6], self=data[7])


def set_config(id, name, roeMin, roeMax, dividendMin, dividendMax, assetToEquityMax, self):
    if name is None:
        name = "default"
    sqlite_tool.operate_one('insert or replace into config '
                            '(id, name, roeMin, roeMax, dividendMin, dividendMax, assetToEquityMax, self) '
                            'values (?,?,?,?, ?,?,?,?)', (id, name, roeMin, roeMax, dividendMin,
                                                        dividendMax, assetToEquityMax, self))


if __name__ == "__main__":
    create_table()
    set_config(1, "default", 5, 10, 2, 10, 2, False)
    set_config(2, "roe_high", 10, 30, 2, 10, 2, False)
    print(get_config())
