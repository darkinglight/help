---
name: "option-documentation"
description: "提供天勤SDK期权文档参考。当用户需要期权策略开发帮助、API使用指导或遇到TqSDK期权函数问题时调用。"
---

# 期权文档参考

提供天勤SDK官方期权文档参考，帮助用户解决问题并学习期权策略开发的最佳实践。

## 何时使用

- 用户使用TqSDK开发期权交易策略
- 用户遇到期权相关API调用错误或问题
- 用户需要期权希腊字母、波动率或定价指导
- 用户想学习期权策略实现
- 用户询问TqSDK期权功能

## 官方文档

**主要参考**: [天勤SDK期权文档](https://doc.shinnytech.com/tqsdk/latest/demo/option_base.html#)

## 核心功能

### 1. 基础期权使用
- **o10**: 获取实时期权报价
- **o20**: 按特定条件查询期权
- **o30**: 查询平值/实值/虚值期权
- **o40**: 计算期权希腊字母
- **o41**: 计算隐含波动率和历史波动率
- **o60**: 获取期权波动率曲面
- **o70**: 期权套利策略
- **o71**: 获取期权链和行权价
- **o72**: 按实值程度分类期权（方法1）
- **o73**: 按实值程度分类期权（方法2）
- **o74**: 计算ETF期权卖方保证金

### 2. 常用API调用

**查询期权：**
```python
# 查询标的的所有期权
options = api.query_options("SHFE.au2012")

# 查询看跌期权
options = api.query_options("SHFE.au2012", option_class="PUT")

# 查询未到期期权
options = api.query_options("SHFE.au2012", expired=False)

# 查询特定行权价的期权
options = api.query_options("SHFE.au2012", strike_price=340)

# 查询沪深300指数期权
options = api.query_options("SSE.000300", exchange_id="CFFEX")

# 查询带行权日限制的ETF期权
options = api.query_options("SSE.510300", exchange_id="SSE", 
                          exercise_year=2020, exercise_month=12)
```

**查询平值期权：**
```python
# 获取平值看涨期权
atm_options = api.query_atm_options("SHFE.au2012", quote.last_price, 0, "CALL")

# 获取实值期权（3、2、1档行权价）
in_money = api.query_atm_options("SHFE.au2012", quote.open, [3, 2, 1], "CALL")

# 获取混合实值程度期权
mixed = api.query_atm_options("SHFE.au2012", quote.open, [1, 0, -1], "CALL")

# 获取虚值期权
out_of_money = api.query_atm_options("SHFE.au2012", quote.last_price, -1, "CALL")
```

**计算希腊字母：**
```python
from tqsdk.ta import OPTION_GREEKS

# 获取期权报价
quote = api.get_quote("SHFE.cu2006C44000")

# 获取期权和标的的K线数据
klines = api.get_kline_serial(["SHFE.cu2006C44000", "SHFE.cu2006"], 24 * 60 * 60, 30)

# 计算希腊字母
greeks = OPTION_GREEKS(klines, quote, 0.025)

# 访问希腊字母值
print(list(greeks["delta"]))
print(list(greeks["theta"]))
print(list(greeks["gamma"]))
print(list(greeks["vega"]))
print(list(greeks["rho"]))
```

**计算隐含波动率：**
```python
from tqsdk.ta import OPTION_IMPV

# 获取期权报价
quote = api.get_quote("SHFE.cu2006C50000")

# 获取K线数据
klines = api.get_kline_serial(["SHFE.cu2006C50000", "SHFE.cu2006"], 24 * 60 * 60, 20)

# 计算隐含波动率
impv = OPTION_IMPV(klines, quote, 0.025)
print(list(impv["impv"] * 100))
```

## 常见问题解决

### 1. "contains non-existent instrument" 错误
- **原因**: 标的合约代码无效
- **解决**: 检查标的期货合约是否存在且活跃交易
- **参考**: 参见o20示例了解正确API用法

### 2. 查询未返回期权
- **原因**: 标的资产可能没有期权或期权交易不活跃
- **解决**: 尝试不同的到期月份或检查资产是否有期权上市
- **参考**: 参见o20了解按到期日过滤期权

### 3. 希腊字母计算错误
- **原因**: K线数据不足或参数值不正确
- **解决**: 确保至少30天的历史数据和正确的无风险利率
- **参考**: 参见o40了解希腊字母计算示例

### 4. 保证金计算问题
- **原因**: 保证金参数不正确或API使用错误
- **解决**: 参考o74了解ETF期权保证金计算
- **参考**: 参见o74了解保证金计算示例

## 最佳实践

1. **始终关闭API连接**以避免资源泄漏
2. **使用try/except块**进行健壮的错误处理
3. **交易前验证合约存在性**
4. **执行期权策略前检查流动性**
5. **监控希腊字母**进行风险管理
6. **使用适当的数据周期**进行波动率计算
7. **实盘交易前用模拟测试策略**

## 实现示例

### 期权日历价差
```python
from tqsdk import TqApi, TqAuth

api = TqApi(auth=TqAuth("username", "password"))

# 查询近月和远月期权
near_options = api.query_options("CFFEX.IO2603")
far_options = api.query_options("CFFEX.IO2606")

# 选择匹配的行权价和类型
# 实现价差逻辑

api.close()
```

### 波动率策略
```python
from tqsdk import TqApi, TqAuth
from tqsdk.ta import OPTION_IMPV

api = TqApi(auth=TqAuth("username", "password"))

# 获取期权和标的数据
option_quote = api.get_quote("CFFEX.IO2603-C-4800")
klines = api.get_kline_serial(["CFFEX.IO2603-C-4800", "CFFEX.IO2603"], 24*60*60, 30)

# 计算隐含波动率
impv = OPTION_IMPV(klines, option_quote, 0.025)

# 实现波动率策略

api.close()
```

## 相关技能

- **option-query**: 特定期权合约查询
- **risk-management**: 期权风险评估
- **backtesting**: 测试期权策略
- **futures-trading**: 相关期货合约
