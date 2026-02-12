#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
沪深300期权日历价差策略demo

日历价差策略：同时卖出近月期权，买入远月期权
利用时间价值衰减速度不同获利

核心API调用：api.query_options("SSE.000300", exchange_id="CFFEX")
"""

from tqsdk import TqApi, TqAuth, TqSim
from datetime import datetime
import time

class CSI300OptionCalendarSpread:
    """沪深300期权日历价差策略类"""
    
    def __init__(self):
        """初始化策略"""
        # 创建API实例，使用模拟交易
        self.api = TqApi(TqSim(), auth=TqAuth("lightdante", "Pk57485748"))
        self.underlying = "SSE.000300"  # 沪深300指数
        self.exchange_id = "CFFEX"  # 中金所
        self.spread_positions = []
        self.running = True
    
    def get_csi300_options(self):
        """获取沪深300期权合约列表
        
        Returns:
            list: 期权合约列表
        """
        print(f"[{datetime.now()}] 查询沪深300期权合约...")
        try:
            # 使用用户指定的API调用方式
            options = self.api.query_options(self.underlying, exchange_id=self.exchange_id)
            print(f"[{datetime.now()}] 找到 {len(options)} 个沪深300期权合约")
            
            if options:
                print(f"[{datetime.now()}] 示例合约:")
                for opt in options[:5]:
                    print(f"  - {opt}")
            
            return options
        except Exception as e:
            print(f"[{datetime.now()}] 查询期权失败: {e}")
            return []
    
    def analyze_options(self, options):
        """分析期权合约
        
        Args:
            options: 期权合约列表
            
        Returns:
            dict: 分析结果
        """
        analysis = {
            "total": len(options),
            "by_expiry": {},  # 按到期日分组
            "by_type": {"CALL": [], "PUT": []},  # 按类型分组
            "by_strike": {}  # 按行权价分组
        }
        
        for opt in options:
            # 解析期权合约代码
            parts = opt.split("-")
            if len(parts) >= 3:
                # 提取信息
                underlying_info = parts[0]
                option_type = parts[1]  # C为看涨，P为看跌
                expiry_strike = parts[2]
                
                # 解析到期日和行权价
                # 合约格式：CFFEX.IO2412-P-2800
                # 其中 IO2412 表示 2024年12月到期
                underlying_parts = underlying_info.split(".")
                if len(underlying_parts) == 2:
                    io_part = underlying_parts[1]
                    if len(io_part) >= 6 and io_part.startswith("IO"):
                        expiry = io_part[2:6]  # 提取到期日，如 IO2412 -> 2412
                        strike = expiry_strike  # 行权价
                        
                        # 按到期日分组
                        if expiry not in analysis["by_expiry"]:
                            analysis["by_expiry"][expiry] = []
                        analysis["by_expiry"][expiry].append(opt)
                        
                        # 按类型分组
                        if option_type == "C":
                            analysis["by_type"]["CALL"].append(opt)
                        elif option_type == "P":
                            analysis["by_type"]["PUT"].append(opt)
                        
                        # 按行权价分组
                        if strike not in analysis["by_strike"]:
                            analysis["by_strike"][strike] = []
                        analysis["by_strike"][strike].append(opt)
        
        return analysis
    
    def select_calendar_spread(self, options):
        """选择日历价差合约
        
        Args:
            options: 期权合约列表
            
        Returns:
            dict: 日历价差信息
        """
        # 按到期日分组
        options_by_expiry = {}
        current_date = datetime.now()
        current_year_month = current_date.strftime("%y%m")
        
        for opt in options:
            parts = opt.split("-")
            if len(parts) >= 3:
                underlying_info = parts[0]
                # 解析到期日
                underlying_parts = underlying_info.split(".")
                if len(underlying_parts) == 2:
                    io_part = underlying_parts[1]
                    if len(io_part) >= 6 and io_part.startswith("IO"):
                        expiry = io_part[2:6]  # 提取到期日，如 IO2412 -> 2412
                        
                        # 过滤掉过期合约
                        if expiry >= current_year_month:
                            if expiry not in options_by_expiry:
                                options_by_expiry[expiry] = []
                            options_by_expiry[expiry].append(opt)
        
        # 排序到期日
        sorted_expiries = sorted(options_by_expiry.keys())
        print(f"[{datetime.now()}] 当前时间: {current_date.strftime('%Y-%m-%d')}")
        print(f"[{datetime.now()}] 可用到期日(未来): {sorted_expiries}")
        
        if len(sorted_expiries) < 2:
            print("[{datetime.now()}] 到期日不足，无法构建日历价差")
            return None
        
        # 选择最近的两个到期日
        near_expiry = sorted_expiries[0]
        far_expiry = sorted_expiries[1]
        
        near_options = options_by_expiry[near_expiry]
        far_options = options_by_expiry[far_expiry]
        
        print(f"[{datetime.now()}] 选择到期日组合:")
        print(f"  近月: {near_expiry} ({len(near_options)}个合约)")
        print(f"  远月: {far_expiry} ({len(far_options)}个合约)")
        
        # 按行权价和类型匹配
        matched_spreads = []
        
        # 为每个近月合约寻找对应的远月合约
        for near_opt in near_options:
            near_parts = near_opt.split("-")
            if len(near_parts) >= 3:
                near_type = near_parts[1]  # 提取期权类型
                near_strike = near_parts[2]  # 提取行权价
                
                # 在远月合约中寻找相同类型和行权价的合约
                for far_opt in far_options:
                    far_parts = far_opt.split("-")
                    if len(far_parts) >= 3:
                        far_type = far_parts[1]  # 提取期权类型
                        far_strike = far_parts[2]  # 提取行权价
                        
                        # 匹配类型和行权价
                        if near_type == far_type and near_strike == far_strike:
                            matched_spreads.append({
                                "type": near_type,
                                "strike": near_strike,
                                "near_expiry": near_expiry,
                                "far_expiry": far_expiry,
                                "near_contract": near_opt,
                                "far_contract": far_opt
                            })
        
        if not matched_spreads:
            print("[{datetime.now()}] 无法找到匹配的日历价差组合")
            return None
        
        # 选择一个合适的价差组合
        # 优先选择平值期权附近的合约
        print(f"[{datetime.now()}] 找到 {len(matched_spreads)} 个匹配的日历价差组合")
        
        # 简单选择第一个组合，实际策略中可以根据波动率、流动性等因素选择
        selected_spread = matched_spreads[0]
        
        print(f"[{datetime.now()}] 选择的日历价差组合:")
        print(f"  期权类型: {'看涨期权' if selected_spread['type'] == 'C' else '看跌期权'}")
        print(f"  行权价: {selected_spread['strike']}")
        print(f"  近月合约: {selected_spread['near_contract']}")
        print(f"  远月合约: {selected_spread['far_contract']}")
        
        return selected_spread
    
    def get_option_quote(self, contract):
        """获取期权合约行情
        
        Args:
            contract: 期权合约代码
            
        Returns:
            dict: 行情信息
        """
        try:
            quote = self.api.get_quote(contract)
            self.api.wait_update()
            
            return {
                "last_price": quote.last_price or 0,
                "bid_price1": quote.bid_price1 or 0,
                "ask_price1": quote.ask_price1 or 0,
                "volume": quote.volume or 0,
                "open_interest": quote.open_interest or 0
            }
        except Exception as e:
            print(f"[{datetime.now()}] 获取行情失败: {e}")
            return {
                "last_price": 0,
                "bid_price1": 0,
                "ask_price1": 0,
                "volume": 0,
                "open_interest": 0
            }
    
    def calculate_spread_price(self, near_contract, far_contract):
        """计算价差价格
        
        Args:
            near_contract: 近月合约代码
            far_contract: 远月合约代码
            
        Returns:
            dict: 价差价格信息
        """
        # 获取近月合约行情
        near_quote = self.get_option_quote(near_contract)
        # 获取远月合约行情
        far_quote = self.get_option_quote(far_contract)
        
        # 计算价差
        spread = {
            "near_bid": near_quote["bid_price1"],
            "near_ask": near_quote["ask_price1"],
            "near_last": near_quote["last_price"],
            "far_bid": far_quote["bid_price1"],
            "far_ask": far_quote["ask_price1"],
            "far_last": far_quote["last_price"],
            "spread_bid": far_quote["bid_price1"] - near_quote["ask_price1"],  # 卖出近月(ask)，买入远月(bid)
            "spread_ask": far_quote["ask_price1"] - near_quote["bid_price1"],  # 卖出近月(bid)，买入远月(ask)
            "spread_last": far_quote["last_price"] - near_quote["last_price"]  # 最新价计算的价差
        }
        
        return spread
    
    def place_spread_order(self, spread):
        """下单日历价差
        
        Args:
            spread: 日历价差信息
            
        Returns:
            bool: 是否下单成功
        """
        if not spread:
            return False
        
        near_contract = spread["near_contract"]
        far_contract = spread["far_contract"]
        
        # 计算价差价格
        spread_price = self.calculate_spread_price(near_contract, far_contract)
        
        print(f"[{datetime.now()}] 当前价差价格:")
        print(f"  近月合约: {near_contract}")
        print(f"    买价: {spread_price['near_bid']:.2f}, 卖价: {spread_price['near_ask']:.2f}, 最新: {spread_price['near_last']:.2f}")
        print(f"  远月合约: {far_contract}")
        print(f"    买价: {spread_price['far_bid']:.2f}, 卖价: {spread_price['far_ask']:.2f}, 最新: {spread_price['far_last']:.2f}")
        print(f"  价差: 买价={spread_price['spread_bid']:.2f}, 卖价={spread_price['spread_ask']:.2f}, 最新={spread_price['spread_last']:.2f}")
        
        # 检查流动性
        near_liquidity = self.get_option_quote(near_contract)["volume"]
        far_liquidity = self.get_option_quote(far_contract)["volume"]
        
        print(f"[{datetime.now()}] 流动性检查:")
        print(f"  近月合约成交量: {near_liquidity}")
        print(f"  远月合约成交量: {far_liquidity}")
        
        if near_liquidity < 10 or far_liquidity < 10:
            print("[{datetime.now()}] 流动性不足，暂不下单")
            return False
        
        # 下单策略：卖出近月期权，买入远月期权
        try:
            print("[{datetime.now()}] 开始下单...")
            
            # 1. 卖出近月期权
            near_order = self.api.insert_order(
                symbol=near_contract,
                direction="SELL",
                offset="OPEN",
                volume=1,
                limit_price=spread_price["near_bid"]  # 以买价卖出
            )
            
            # 2. 买入远月期权
            far_order = self.api.insert_order(
                symbol=far_contract,
                direction="BUY",
                offset="OPEN",
                volume=1,
                limit_price=spread_price["far_ask"]  # 以卖价买入
            )
            
            # 等待订单成交
            print("[{datetime.now()}] 等待订单成交...")
            start_time = time.time()
            timeout = 60  # 60秒超时
            
            while time.time() - start_time < timeout:
                self.api.wait_update()
                
                near_status = getattr(near_order, "status", "UNKNOWN")
                far_status = getattr(far_order, "status", "UNKNOWN")
                
                print(f"[{datetime.now()}] 订单状态 - 近月: {near_status}, 远月: {far_status}")
                
                if near_status == "FINISHED" and far_status == "FINISHED":
                    print("[{datetime.now()}] 日历价差下单完成！")
                    self.spread_positions.append(spread)
                    return True
                
                time.sleep(2)
            
            print("[{datetime.now()}] 订单超时未成交")
            return False
            
        except Exception as e:
            print(f"[{datetime.now()}] 下单失败: {e}")
            return False
    
    def monitor_spread(self):
        """监控日历价差"""
        while self.running:
            try:
                if not self.spread_positions:
                    print("[{datetime.now()}] 无持仓需要监控")
                    time.sleep(10)
                    continue
                
                for i, spread in enumerate(self.spread_positions):
                    # 获取行情
                    near_quote = self.get_option_quote(spread["near_contract"])
                    far_quote = self.get_option_quote(spread["far_contract"])
                    
                    # 计算价差
                    current_spread = far_quote["last_price"] - near_quote["last_price"]
                    
                    print(f"\n[{datetime.now()}] 日历价差监控 #{i+1}")
                    print(f"  期权类型: {'看涨期权' if spread['type'] == 'C' else '看跌期权'}")
                    print(f"  行权价: {spread['strike']}")
                    print(f"  近月合约: {spread['near_contract']}")
                    print(f"    最新价: {near_quote['last_price']:.2f}, 成交量: {near_quote['volume']}")
                    print(f"  远月合约: {spread['far_contract']}")
                    print(f"    最新价: {far_quote['last_price']:.2f}, 成交量: {far_quote['volume']}")
                    print(f"  当前价差: {current_spread:.2f}")
                
                time.sleep(15)  # 每15秒监控一次
                
            except KeyboardInterrupt:
                print("[{datetime.now()}] 监控已停止")
                break
            except Exception as e:
                print(f"[{datetime.now()}] 监控出错: {e}")
                time.sleep(5)
    
    def close_positions(self):
        """平仓所有持仓"""
        print("[{datetime.now()}] 开始平仓...")
        
        for spread in self.spread_positions:
            try:
                # 平仓近月合约（买入）
                near_contract = spread["near_contract"]
                near_order = self.api.insert_order(
                    symbol=near_contract,
                    direction="BUY",
                    offset="CLOSE",
                    volume=1,
                    limit_price=self.get_option_quote(near_contract)["ask_price1"]
                )
                
                # 平仓远月合约（卖出）
                far_contract = spread["far_contract"]
                far_order = self.api.insert_order(
                    symbol=far_contract,
                    direction="SELL",
                    offset="CLOSE",
                    volume=1,
                    limit_price=self.get_option_quote(far_contract)["bid_price1"]
                )
                
                # 等待平仓完成
                start_time = time.time()
                while time.time() - start_time < 30:
                    self.api.wait_update()
                    if (getattr(near_order, "status", "") == "FINISHED" and 
                        getattr(far_order, "status", "") == "FINISHED"):
                        print(f"[{datetime.now()}] 平仓完成: {spread['near_contract']} 和 {spread['far_contract']}")
                        break
                    time.sleep(1)
                
            except Exception as e:
                print(f"[{datetime.now()}] 平仓失败: {e}")
        
        self.spread_positions = []
    
    def run_strategy(self):
        """运行策略"""
        print(f"[{datetime.now()}] 启动沪深300期权日历价差策略")
        print(f"[{datetime.now()}] 使用API调用: api.query_options('{self.underlying}', exchange_id='{self.exchange_id}')")
        
        try:
            # 1. 查询沪深300期权合约
            options = self.get_csi300_options()
            
            if not options:
                print("[{datetime.now()}] 未找到沪深300期权合约")
                return False
            
            # 2. 分析期权合约
            analysis = self.analyze_options(options)
            print(f"[{datetime.now()}] 期权合约分析:")
            print(f"  总合约数: {analysis['total']}")
            print(f"  看涨期权: {len(analysis['by_type']['CALL'])}")
            print(f"  看跌期权: {len(analysis['by_type']['PUT'])}")
            print(f"  到期日数量: {len(analysis['by_expiry'])}")
            
            # 3. 选择日历价差组合
            spread = self.select_calendar_spread(options)
            
            if not spread:
                print("[{datetime.now()}] 无法选择日历价差组合")
                return False
            
            # 4. 下单
            success = self.place_spread_order(spread)
            
            if not success:
                print("[{datetime.now()}] 下单失败")
                return False
            
            # 5. 监控
            print("\n[{datetime.now()}] 开始监控日历价差...")
            print("[{datetime.now()}] 按 Ctrl+C 停止监控并平仓")
            
            try:
                self.monitor_spread()
            except KeyboardInterrupt:
                print("[{datetime.now()}] 收到停止信号")
            
            # 6. 平仓
            self.close_positions()
            
            return True
            
        except Exception as e:
            print(f"[{datetime.now()}] 策略运行出错: {e}")
            return False
        finally:
            self.running = False
            self.api.close()
            print("[{datetime.now()}] API连接已关闭")

if __name__ == "__main__":
    print("="*60)
    print("沪深300期权日历价差策略demo")
    print("="*60)
    print("策略说明:")
    print("1. 使用 api.query_options('SSE.000300', exchange_id='CFFEX') 查询沪深300期权")
    print("2. 卖出近月期权，买入远月期权")
    print("3. 利用时间价值衰减速度不同获利")
    print("="*60)
    
    # 运行策略
    strategy = CSI300OptionCalendarSpread()
    strategy.run_strategy()
    
    print("\n" + "="*60)
    print("策略执行完成")
    print("="*60)
    print("后续优化方向:")
    print("1. 添加波动率分析，选择高隐含波动率的合约")
    print("2. 实现自动止损止盈逻辑")
    print("3. 添加多组价差组合的管理")
    print("4. 优化下单算法，提高成交率")
    print("5. 添加回测功能，评估策略历史表现")
