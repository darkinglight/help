---
name: "option-query"
description: "提供期权查询功能，包括沪深300期权。当用户需要查询期权合约时调用，特别是使用 api.query_options("SSE.000300", exchange_id="CFFEX") 查询沪深300期权。"
---

# 期权查询功能

提供各类标的资产的期权合约查询和分析功能，重点关注沪深300指数期权。

## 何时使用

- 用户需要查询特定标的资产的期权合约
- 用户想要分析期权链和价差策略
- 用户询问沪深300期权
- 用户需要期权交易策略的代码示例

## 核心功能

### 1. 沪深300期权查询

**重要API调用：**

```python
from tqsdk import TqApi, TqAuth

api = TqApi(auth=TqAuth("username", "password"))
ls = api.query_options("SSE.000300", exchange_id="CFFEX")
print(ls)  # 中金所沪深300股指期权
api.close()
```

### 2. 其他标的资产

支持查询多种标的资产的期权：
- **中证1000**: `api.query_options("SSE.000852")`
- **上证50**: `api.query_options("SSE.000016")`
- **中证500**: `api.query_options("SSE.000905")`

### 3. 期权合约格式

- **格式**: `交易所.标的-类型-到期日行权价`
- **示例**: `CFFEX.IO2603-C-4800`（沪深300看涨期权，2026年3月到期，4800行权价）

### 4. 策略示例

**日历价差策略：**
```python
def create_calendar_spread(api, underlying):
    """通过卖出近月期权、买入远月期权创建日历价差"""
    options = api.query_options(underlying)
    # 按到期日分析期权
    # 选择匹配的行权价
    # 执行价差订单
    return spread_info
```

**垂直价差策略：**
```python
def create_vertical_spread(api, underlying, spread_type):
    """创建牛市/熊市垂直价差"""
    options = api.query_options(underlying)
    # 选择不同行权价的期权
    # 执行价差订单
    return spread_info
```

## 使用示例

### 示例1：查询沪深300期权

**用户请求：** "我需要获取所有沪深300期权合约"

**响应：**
```python
from tqsdk import TqApi, TqAuth

# 初始化API
api = TqApi(auth=TqAuth("your_username", "your_password"))

# 查询沪深300期权
print("查询沪深300期权...")
try:
    options = api.query_options("SSE.000300", exchange_id="CFFEX")
    print(f"找到 {len(options)} 个沪深300期权合约")
    if options:
        print("示例合约:")
        for opt in options[:5]:
            print(f"  - {opt}")
except Exception as e:
    print(f"查询期权失败: {e}")
finally:
    api.close()
```

### 示例2：分析期权链

**用户请求：** "分析沪深300 2026年3月到期的期权链"

**响应：**
```python
from tqsdk import TqApi, TqAuth

api = TqApi(auth=TqAuth("your_username", "your_password"))

try:
    # 查询期权
    options = api.query_options("SSE.000300", exchange_id="CFFEX")
    
    # 过滤2026年3月到期
    march_options = [opt for opt in options if "2603" in opt]
    
    # 分离看涨和看跌期权
    calls = [opt for opt in march_options if "-C-" in opt]
    puts = [opt for opt in march_options if "-P-" in opt]
    
    print(f"2026年3月期权分析:")
    print(f"总合约数: {len(march_options)}")
    print(f"看涨期权: {len(calls)}")
    print(f"看跌期权: {len(puts)}")
    
    # 获取行权价
    strikes = sorted(list(set([opt.split("-")[2] for opt in march_options])))
    print(f"可用行权价: {strikes}")
    
finally:
    api.close()
```

## 常见错误处理

1. **"contains non-existent instrument"**
   - 检查标的合约是否存在
   - 验证合约代码格式
   - 尝试不同的到期月份

2. **"no options found"**
   - 确认标的资产有期权
   - 检查期权交易是否活跃
   - 尝试不同的API参数

3. **网络/连接问题**
   - 检查网络连接
   - 验证TqAuth凭据
   - 使用指数退避重试

## 最佳实践

1. **始终关闭API连接**以避免资源泄漏
2. **使用try/except块**进行健壮的错误处理
3. **交易前验证合约存在性**
4. **执行策略前监控期权流动性**
5. **持有期权头寸时考虑时间衰减**

## 依赖项

- **tqsdk**: 期权数据和交易必需
- **Python 3.8+**: 推荐以获得最佳兼容性
- **网络连接**: 实时数据必需

## 相关技能

- **futures-trading**: 期货合约分析
- **risk-management**: 期权风险评估
- **backtesting**: 测试期权策略
