#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'ringo'

from tqsdk import TqApi, TqAuth
from tqsdk.ta import OPTION_IMPV

api = TqApi(auth=TqAuth("lightdante", "Pk57485748"))

# 获取指定期权行情
quote = api.get_quote("CFFEX.IO2603-C-4700")

# 获取期权和对应标的的多合约 kline
klines = api.get_kline_serial(["CFFEX.IO2603-C-4700", "SSE.000300"], 24 * 60 * 60, 20)

# 通过 OPTION_IMPV 函数计算隐含波动率，设置无风险利率为 0.025
impv = OPTION_IMPV(klines, quote, 0.025)

print(list(impv["impv"] * 100))

api.close()