#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
测试合约到期日解析逻辑
"""

import re
from datetime import datetime

# 测试合约解析
test_contracts = [
    "CFFEX.MO2506-P-7100",  # 25年6月到期的看跌期权
    "CFFEX.MO2503-C-6800",  # 25年3月到期的看涨期权
    "CFFEX.MO2606-P-7500",  # 26年6月到期的看跌期权
    "CFFEX.MO2603-C-7200",  # 26年3月到期的看涨期权
    "CFFEX.IM2603-C-7000",  # IM开头的合约
]

print("="*60)
print("测试合约到期日解析")
print("="*60)

for opt in test_contracts:
    try:
        # 解析合约代码
        parts = opt.split("-")
        if len(parts) >= 3:
            underlying_info = parts[0]
            
            # 提取到期月 - 处理 IM 开头的合约
            if "IM" in underlying_info:
                match = re.search(r"IM(\d{4})", underlying_info)
                if match:
                    expiry = match.group(1)
                    print(f"解析合约 {opt}，到期日: {expiry}")
            # 处理 MO 开头的合约
            elif "MO" in underlying_info:
                match = re.search(r"MO(\d{4})", underlying_info)
                if match:
                    expiry = match.group(1)
                    print(f"解析合约 {opt}，到期日: {expiry}")
            else:
                print(f"无法解析合约 {opt}")
        else:
            print(f"合约格式不正确: {opt}")
    except Exception as e:
        print(f"解析合约 {opt} 失败: {e}")

print("="*60)
print("测试完成")
print("="*60)
