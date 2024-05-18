from collections import namedtuple

from SqliteTool import SqliteTool

sqlite_tool = SqliteTool()

Config = namedtuple("Config", ['name', 'roeMin', 'roeMax',
                               'dividendMin', 'dividendMax', 'assetToEquityMax', 'self'])


def create_table():
    # 创建数据表dividend的SQL语句
    create_tb_sql = ("create table if not exists config ("
                     "name text PRIMARY KEY,"
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


def get_config():
    name = "default"
    data = sqlite_tool.query_one("select * from config where name = :name", {"name": name})
    if data is None:
        return None
    return Config(name=data[0], roeMin=data[1], roeMax=data[2], dividendMin=data[3],
                  dividendMax=data[4], assetToEquityMax=data[5], self=data[6])


def set_config(roeMin, roeMax, dividendMin, dividendMax, assetToEquityMax, self):
    name = "default"
    sqlite_tool.operate_one('insert or replace into config '
                            '(name, roeMin, roeMax, dividendMin, dividendMax, assetToEquityMax, self) '
                            'values (?,?,?, ?,?,?,?)', (name, roeMin, roeMax, dividendMin,
                                                        dividendMax, assetToEquityMax, self))


if __name__ == "__main__":
    create_table()
    set_config(10, 30, 2, 10, 2, False)
    print(get_config())
