from SqliteTool import SqliteTool
from baseinfo import baseinfo

sqliteTool = SqliteTool()


def init_table():
    # 创建数据表info的SQL语句
    create_tb_sql = ("create table if not exists self ("
                     "code text primary key,"
                     "name text"
                     ");")
    # 创建数据表
    sqliteTool.drop_table("drop table self;")
    sqliteTool.create_table(create_tb_sql)


def self_add(code, name):
    sqliteTool.operate_one('insert into self values(?,?)', (code, name))


def self_delete(code):
    sqliteTool.delete_record(f"delete from self where code = '{code}'")


def self_alter(code):
    if self_get(code) is None:
        info_data = baseinfo(code)
        self_add(code, info_data.name)
    else:
        self_delete(code)


def self_get(code):
    data = sqliteTool.query_one(f"select code from self where code = '{code}'")
    if data is None:
        return None
    return data[0]


def self_list_code():
    datas = sqliteTool.query_many("select code from self")
    result = []
    for item in datas:
        result.append(item[0])
    return result


if __name__ == '__main__':
    # init_table()
    # self_add("sh.600741", "华域汽车")
    # delete_self("sh.600741")
    print(self_list_code())
