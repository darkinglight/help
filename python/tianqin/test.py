#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'chengzhi'

from tqsdk import TqApi, TqAuth

# 创建API实例,传入自己的快期账户
api = TqApi(auth=TqAuth("lightdante", "Pk57485748"))

# 中金所沪深300股指期权
ls = api.query_options("SSE.000300")
print(ls)

# # 获得上期所 ni2206 的行情引用，当行情有变化时 quote 中的字段会对应更新
# quote = api.get_quote("CFFEX.MO2603-C-8300")
# # 输出 ni2206 的最新行情时间和最新价
# print(quote.datetime, quote.last_price)

# 关闭api,释放资源
api.close()