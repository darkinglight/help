#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
中证1000期权日历价差策略demo

策略说明：
1. 卖出3月到期的中证1000期权
2. 买入6月到期的中证1000期权
3. 利用时间价值衰减速度不同获利

标的：中证1000指数期权 (CFFEX.IM)
"""

# 模块导入检查
try:
    from tqsdk import TqApi, TqAuth, TqSim
except ImportError:
    print("错误: 未找到 tqsdk 模块，请先安装")
    print("安装命令: pip install tqsdk")
    exit(1)

from datetime import datetime
import time
import re
import sys

class CSI1000OptionCalendarSpread:
    """中证1000期权日历价差策略类"""
    
    def __init__(self, username="lightdante", password="Pk57485748", near_month="2603", far_month="2606"):
        """初始化策略
        
        Args:
            username: 快期账户用户名
            password: 快期账户密码
            near_month: 近月到期日（格式：YYMM，如2603）
            far_month: 远月到期日（格式：YYMM，如2606）
        """
        try:
            # 创建API实例，使用模拟交易
            print(f"[{datetime.now()}] 初始化TqApi...")
            self.api = TqApi(TqSim(), auth=TqAuth(username, password))
            print(f"[{datetime.now()}] TqApi初始化成功")
        except Exception as e:
            print(f"[{datetime.now()}] TqApi初始化失败: {e}")
            raise
        
        self.underlying = "CFFEX.IM"  # 中证1000期货
        self.near_month = near_month  # 3月到期
        self.far_month = far_month  # 6月到期
        self.spread_positions = []
        self.running = True
        self.username = username
        self.password = password
        
        print(f"[{datetime.now()}] 策略配置:")
        print(f"  近月到期: {self.near_month}")
        print(f"  远月到期: {self.far_month}")
    
    def get_csi1000_options(self):
        """获取中证1000期权合约列表
        
        Returns:
            list: 期权合约列表
        """
        print(f"[{datetime.now()}] 查询中证1000期权合约...")
        
        all_options = []
        
        try:
            # 只使用中证1000指数代码查询
            test_underlyings = [
                "SSE.000852"  # 中证1000指数
            ]
            
            # 去重，避免重复查询
            test_underlyings = list(set(test_underlyings))
            
            print(f"[{datetime.now()}] 准备查询 {len(test_underlyings)} 个标的")
            
            for underlying in test_underlyings:
                print(f"[{datetime.now()}] 尝试查询: {underlying}")
                try:
                    # 使用正确的API调用方式
                    options = self.api.query_options(underlying)
                    
                    # 检查返回值
                    if isinstance(options, list):
                        print(f"[{datetime.now()}] 找到 {len(options)} 个合约")
                        all_options.extend(options)
                    else:
                        print(f"[{datetime.now()}] 查询 {underlying} 返回非列表类型: {type(options)}")
                        
                except Exception as e:
                    print(f"[{datetime.now()}] 查询 {underlying} 失败: {e}")
                    # 继续查询其他标的
                    continue
            
            # 去重
            all_options = list(set(all_options))
            print(f"[{datetime.now()}] 总计找到 {len(all_options)} 个中证1000期权合约")
            
            if all_options:
                print(f"[{datetime.now()}] 示例合约:")
                for opt in all_options[:5]:
                    print(f"  - {opt}")
            else:
                print(f"[{datetime.now()}] 未找到任何中证1000期权合约")
            
            return all_options
            
        except Exception as e:
            print(f"[{datetime.now()}] 查询期权失败: {e}")
            import traceback
            traceback.print_exc()
            return []
    
    def filter_options_by_month(self, options):
        """按到期月过滤期权合约
        
        Args:
            options: 期权合约列表
            
        Returns:
            dict: 包含近月和远月合约的字典
        """
        filtered = {
            "near": [],  # 3月到期
            "far": []   # 6月到期
        }
        
        print(f"[{datetime.now()}] 过滤期权合约，近月={self.near_month}, 远月={self.far_month}")
        
        for opt in options:
            try:
                # 解析合约代码
                parts = opt.split("-")
                if len(parts) >= 3:
                    underlying_info = parts[0]
                    
                    # 提取到期月 - 方法1：从合约代码中提取
                    # 处理 IM 开头的合约
                    if "IM" in underlying_info:
                        match = re.search(r"IM(\d{4})", underlying_info)
                        if match:
                            expiry = match.group(1)
                            print(f"[{datetime.now()}] 解析合约 {opt}，到期日: {expiry}")
                            if expiry == self.near_month:
                                filtered["near"].append(opt)
                                print(f"[{datetime.now()}] 添加到近月合约: {opt}")
                            elif expiry == self.far_month:
                                filtered["far"].append(opt)
                                print(f"[{datetime.now()}] 添加到远月合约: {opt}")
                    # 处理 MO 开头的合约
                    elif "MO" in underlying_info:
                        match = re.search(r"MO(\d{4})", underlying_info)
                        if match:
                            expiry = match.group(1)
                            print(f"[{datetime.now()}] 解析合约 {opt}，到期日: {expiry}")
                            if expiry == self.near_month:
                                filtered["near"].append(opt)
                                print(f"[{datetime.now()}] 添加到近月合约: {opt}")
                            elif expiry == self.far_month:
                                filtered["far"].append(opt)
                                print(f"[{datetime.now()}] 添加到远月合约: {opt}")
            
            except Exception as e:
                print(f"[{datetime.now()}] 解析合约 {opt} 失败: {e}")
                continue
        
        # 打印结果
        print(f"[{datetime.now()}] 过滤结果:")
        print(f"  3月到期合约: {len(filtered['near'])}")
        print(f"  6月到期合约: {len(filtered['far'])}")
        
        # 打印前几个合约示例
        if filtered["near"]:
            print(f"[{datetime.now()}] 3月合约示例:")
            for opt in filtered["near"][:3]:
                print(f"  - {opt}")
        
        if filtered["far"]:
            print(f"[{datetime.now()}] 6月合约示例:")
            for opt in filtered["far"][:3]:
                print(f"  - {opt}")
        
        return filtered
    
    def select_calendar_spread(self, near_options, far_options):
        """选择日历价差合约
        
        Args:
            near_options: 近月合约列表
            far_options: 远月合约列表
            
        Returns:
            dict: 日历价差信息
        """
        matched_spreads = []
        
        print(f"[{datetime.now()}] 选择日历价差组合，近月合约数={len(near_options)}, 远月合约数={len(far_options)}")
        
        # 为每个近月合约寻找对应的远月合约
        for near_opt in near_options:
            try:
                near_parts = near_opt.split("-")
                if len(near_parts) >= 3:
                    near_type = near_parts[1]  # 期权类型
                    near_strike = near_parts[2]  # 行权价
                    
                    print(f"[{datetime.now()}] 处理近月合约: {near_opt}, 类型={near_type}, 行权价={near_strike}")
                    
                    # 在远月合约中寻找相同类型和行权价的合约
                    for far_opt in far_options:
                        try:
                            far_parts = far_opt.split("-")
                            if len(far_parts) >= 3:
                                far_type = far_parts[1]
                                far_strike = far_parts[2]
                                
                                # 匹配类型和行权价
                                if near_type == far_type and near_strike == far_strike:
                                    print(f"[{datetime.now()}] 找到匹配: 远月合约={far_opt}")
                                    matched_spreads.append({
                                        "type": near_type,
                                        "strike": near_strike,
                                        "near_contract": near_opt,
                                        "far_contract": far_opt
                                    })
                        except Exception as e:
                            print(f"[{datetime.now()}] 处理远月合约 {far_opt} 失败: {e}")
                            continue
            except Exception as e:
                print(f"[{datetime.now()}] 处理近月合约 {near_opt} 失败: {e}")
                continue
        
        if not matched_spreads:
            print(f"[{datetime.now()}] 无法找到匹配的日历价差组合")
            return None
        
        print(f"[{datetime.now()}] 找到 {len(matched_spreads)} 个匹配的日历价差组合")
        
        # 打印所有匹配的组合
        print(f"[{datetime.now()}] 匹配的日历价差组合:")
        for i, spread in enumerate(matched_spreads[:5]):  # 只打印前5个
            print(f"  {i+1}. 类型: {'C' if spread['type'] == 'C' else 'P'}, 行权价: {spread['strike']}")
            print(f"     3月: {spread['near_contract']}")
            print(f"     6月: {spread['far_contract']}")
        
        if len(matched_spreads) > 5:
            print(f"[{datetime.now()}] ... 还有 {len(matched_spreads) - 5} 个组合")
        
        # 选择一个合适的组合
        # 优先选择平值附近的合约
        selected_spread = matched_spreads[len(matched_spreads)//2]
        
        print(f"[{datetime.now()}] 选择的日历价差组合:")
        print(f"  期权类型: {'看涨期权' if selected_spread['type'] == 'C' else '看跌期权'}")
        print(f"  行权价: {selected_spread['strike']}")
        print(f"  3月合约(卖出): {selected_spread['near_contract']}")
        print(f"  6月合约(买入): {selected_spread['far_contract']}")
        
        return selected_spread
    
    def get_option_quote(self, contract):
        """获取期权合约行情
        
        Args:
            contract: 期权合约代码
            
        Returns:
            dict: 行情信息
        """
        try:
            print(f"[{datetime.now()}] 获取合约行情: {contract}")
            quote = self.api.get_quote(contract)
            
            # 等待行情更新
            start_time = time.time()
            timeout = 5  # 5秒超时
            while time.time() - start_time < timeout:
                updated = self.api.wait_update()
                if updated:
                    break
                time.sleep(0.1)
            
            # 构建返回结果
            result = {
                "last_price": 0,
                "bid_price1": 0,
                "ask_price1": 0,
                "volume": 0,
                "open_interest": 0
            }
            
            # 安全获取属性
            if hasattr(quote, "last_price") and quote.last_price is not None:
                result["last_price"] = float(quote.last_price)
            
            if hasattr(quote, "bid_price1") and quote.bid_price1 is not None:
                result["bid_price1"] = float(quote.bid_price1)
            
            if hasattr(quote, "ask_price1") and quote.ask_price1 is not None:
                result["ask_price1"] = float(quote.ask_price1)
            
            if hasattr(quote, "volume") and quote.volume is not None:
                result["volume"] = int(quote.volume)
            
            if hasattr(quote, "open_interest") and quote.open_interest is not None:
                result["open_interest"] = int(quote.open_interest)
            
            print(f"[{datetime.now()}] 行情获取成功: {contract}")
            print(f"  最新价: {result['last_price']}, 买价: {result['bid_price1']}, 卖价: {result['ask_price1']}")
            print(f"  成交量: {result['volume']}, 持仓量: {result['open_interest']}")
            
            return result
            
        except Exception as e:
            print(f"[{datetime.now()}] 获取行情失败: {e}")
            import traceback
            traceback.print_exc()
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
        print(f"[{datetime.now()}] 计算价差价格")
        print(f"  近月合约: {near_contract}")
        print(f"  远月合约: {far_contract}")
        
        # 获取行情
        near_quote = self.get_option_quote(near_contract)
        far_quote = self.get_option_quote(far_contract)
        
        try:
            # 计算价差
            spread = {
                "near_bid": near_quote["bid_price1"],
                "near_ask": near_quote["ask_price1"],
                "near_last": near_quote["last_price"],
                "far_bid": far_quote["bid_price1"],
                "far_ask": far_quote["ask_price1"],
                "far_last": far_quote["last_price"],
                "spread_bid": far_quote["bid_price1"] - near_quote["ask_price1"],
                "spread_ask": far_quote["ask_price1"] - near_quote["bid_price1"],
                "spread_last": far_quote["last_price"] - near_quote["last_price"]
            }
            
            # 验证价差计算
            print(f"[{datetime.now()}] 价差计算结果:")
            print(f"  近月 - 买价: {spread['near_bid']:.2f}, 卖价: {spread['near_ask']:.2f}, 最新: {spread['near_last']:.2f}")
            print(f"  远月 - 买价: {spread['far_bid']:.2f}, 卖价: {spread['far_ask']:.2f}, 最新: {spread['far_last']:.2f}")
            print(f"  价差 - 买价: {spread['spread_bid']:.2f}, 卖价: {spread['spread_ask']:.2f}, 最新: {spread['spread_last']:.2f}")
            
            return spread
            
        except Exception as e:
            print(f"[{datetime.now()}] 计算价差失败: {e}")
            # 返回默认值
            return {
                "near_bid": 0,
                "near_ask": 0,
                "near_last": 0,
                "far_bid": 0,
                "far_ask": 0,
                "far_last": 0,
                "spread_bid": 0,
                "spread_ask": 0,
                "spread_last": 0
            }
    
    def place_spread_order(self, spread):
        """下单日历价差
        
        Args:
            spread: 日历价差信息
            
        Returns:
            bool: 是否下单成功
        """
        if not spread:
            print("[{datetime.now()}] 价差信息为空")
            return False
        
        near_contract = spread["near_contract"]
        far_contract = spread["far_contract"]
        
        print(f"[{datetime.now()}] 准备下单日历价差")
        print(f"  3月合约(卖出): {near_contract}")
        print(f"  6月合约(买入): {far_contract}")
        
        # 计算价差价格
        spread_price = self.calculate_spread_price(near_contract, far_contract)
        
        print(f"[{datetime.now()}] 当前价差价格:")
        print(f"  3月合约(卖出): {near_contract}")
        print(f"    买价: {spread_price['near_bid']:.2f}, 卖价: {spread_price['near_ask']:.2f}, 最新: {spread_price['near_last']:.2f}")
        print(f"  6月合约(买入): {far_contract}")
        print(f"    买价: {spread_price['far_bid']:.2f}, 卖价: {spread_price['far_ask']:.2f}, 最新: {spread_price['far_last']:.2f}")
        print(f"  价差: 买价={spread_price['spread_bid']:.2f}, 卖价={spread_price['spread_ask']:.2f}, 最新={spread_price['spread_last']:.2f}")
        
        # 检查流动性
        near_liquidity = self.get_option_quote(near_contract)["volume"]
        far_liquidity = self.get_option_quote(far_contract)["volume"]
        
        print(f"[{datetime.now()}] 流动性检查:")
        print(f"  3月合约成交量: {near_liquidity}")
        print(f"  6月合约成交量: {far_liquidity}")
        
        if near_liquidity < 1 or far_liquidity < 1:
            print("[{datetime.now()}] 流动性不足，暂不下单")
            return False
        
        # 检查价格有效性
        if spread_price["near_bid"] <= 0 or spread_price["far_ask"] <= 0:
            print("[{datetime.now()}] 价格无效，暂不下单")
            return False
        
        # 下单
        try:
            print("[{datetime.now()}] 开始下单...")
            
            # 1. 卖出3月期权
            print("[{datetime.now()}] 下单1: 卖出3月期权")
            near_order = self.api.insert_order(
                symbol=near_contract,
                direction="SELL",
                offset="OPEN",
                volume=1,
                limit_price=spread_price["near_bid"]  # 以买价卖出
            )
            
            # 2. 买入6月期权
            print("[{datetime.now()}] 下单2: 买入6月期权")
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
                try:
                    updated = self.api.wait_update()
                    if updated:
                        near_status = getattr(near_order, "status", "UNKNOWN")
                        far_status = getattr(far_order, "status", "UNKNOWN")
                        
                        print(f"[{datetime.now()}] 订单状态 - 3月: {near_status}, 6月: {far_status}")
                        
                        if near_status == "FINISHED" and far_status == "FINISHED":
                            print("[{datetime.now()}] 日历价差下单完成！")
                            self.spread_positions.append(spread)
                            return True
                except Exception as e:
                    print(f"[{datetime.now()}] 检查订单状态失败: {e}")
                
                time.sleep(1)
            
            print("[{datetime.now()}] 订单超时未成交")
            return False
            
        except Exception as e:
            print(f"[{datetime.now()}] 下单失败: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def monitor_positions(self):
        """监控持仓"""
        while self.running:
            try:
                if not self.spread_positions:
                    print(f"[{datetime.now()}] 无持仓需要监控")
                    time.sleep(10)
                    continue
                
                for i, spread in enumerate(self.spread_positions):
                    try:
                        # 获取行情
                        near_quote = self.get_option_quote(spread["near_contract"])
                        far_quote = self.get_option_quote(spread["far_contract"])
                        
                        # 计算价差
                        current_spread = far_quote["last_price"] - near_quote["last_price"]
                        
                        print(f"\n[{datetime.now()}] 日历价差监控 #{i+1}")
                        print(f"  期权类型: {'看涨期权' if spread['type'] == 'C' else '看跌期权'}")
                        print(f"  行权价: {spread['strike']}")
                        print(f"  3月合约(卖出): {spread['near_contract']}")
                        print(f"    最新价: {near_quote['last_price']:.2f}, 成交量: {near_quote['volume']}")
                        print(f"  6月合约(买入): {spread['far_contract']}")
                        print(f"    最新价: {far_quote['last_price']:.2f}, 成交量: {far_quote['volume']}")
                        print(f"  当前价差: {current_spread:.2f}")
                    except Exception as e:
                        print(f"[{datetime.now()}] 监控持仓 {i+1} 失败: {e}")
                        import traceback
                        traceback.print_exc()
                        continue
                
                print(f"[{datetime.now()}] 等待15秒后再次监控...")
                time.sleep(15)  # 每15秒监控一次
                
            except KeyboardInterrupt:
                print(f"[{datetime.now()}] 监控已停止")
                break
            except Exception as e:
                print(f"[{datetime.now()}] 监控出错: {e}")
                import traceback
                traceback.print_exc()
                print(f"[{datetime.now()}] 等待5秒后重试...")
                time.sleep(5)
    
    def close_positions(self):
        """平仓所有持仓"""
        print(f"[{datetime.now()}] 开始平仓...")
        
        if not self.spread_positions:
            print(f"[{datetime.now()}] 无持仓需要平仓")
            return
        
        for i, spread in enumerate(self.spread_positions):
            try:
                print(f"[{datetime.now()}] 平持仓 {i+1}:")
                print(f"  3月合约: {spread['near_contract']}")
                print(f"  6月合约: {spread['far_contract']}")
                
                # 平仓3月合约（买入）
                near_contract = spread["near_contract"]
                near_quote = self.get_option_quote(near_contract)
                near_order = self.api.insert_order(
                    symbol=near_contract,
                    direction="BUY",
                    offset="CLOSE",
                    volume=1,
                    limit_price=near_quote["ask_price1"]
                )
                
                # 平仓6月合约（卖出）
                far_contract = spread["far_contract"]
                far_quote = self.get_option_quote(far_contract)
                far_order = self.api.insert_order(
                    symbol=far_contract,
                    direction="SELL",
                    offset="CLOSE",
                    volume=1,
                    limit_price=far_quote["bid_price1"]
                )
                
                # 等待平仓完成
                start_time = time.time()
                timeout = 30  # 30秒超时
                while time.time() - start_time < timeout:
                    try:
                        updated = self.api.wait_update()
                        if updated:
                            near_status = getattr(near_order, "status", "UNKNOWN")
                            far_status = getattr(far_order, "status", "UNKNOWN")
                            
                            print(f"[{datetime.now()}] 平仓状态 - 3月: {near_status}, 6月: {far_status}")
                            
                            if near_status == "FINISHED" and far_status == "FINISHED":
                                print(f"[{datetime.now()}] 平仓完成: {spread['near_contract']} 和 {spread['far_contract']}")
                                break
                    except Exception as e:
                        print(f"[{datetime.now()}] 检查平仓状态失败: {e}")
                    
                    time.sleep(1)
                
            except Exception as e:
                print(f"[{datetime.now()}] 平仓失败: {e}")
                import traceback
                traceback.print_exc()
        
        self.spread_positions = []
        print(f"[{datetime.now()}] 所有持仓已平仓")
    
    def run_strategy(self):
        """运行策略"""
        print(f"[{datetime.now()}] 启动中证1000期权日历价差策略")
        print(f"[{datetime.now()}] 策略: 卖出3月期权，买入6月期权")
        
        try:
            # 1. 查询中证1000期权合约
            options = self.get_csi1000_options()
            
            if not options:
                print(f"[{datetime.now()}] 未找到中证1000期权合约")
                return False
            
            # 2. 按到期月过滤合约
            filtered = self.filter_options_by_month(options)
            
            if not filtered["near"] or not filtered["far"]:
                print(f"[{datetime.now()}] 缺少3月或6月到期的合约")
                print(f"  3月合约数: {len(filtered['near'])}")
                print(f"  6月合约数: {len(filtered['far'])}")
                return False
            
            # 3. 选择日历价差组合
            spread = self.select_calendar_spread(filtered["near"], filtered["far"])
            
            if not spread:
                print(f"[{datetime.now()}] 无法选择日历价差组合")
                return False
            
            # 4. 下单
            success = self.place_spread_order(spread)
            
            if not success:
                print(f"[{datetime.now()}] 下单失败")
                return False
            
            # 5. 监控
            print("\n[{datetime.now()}] 开始监控日历价差...")
            print("[{datetime.now()}] 按 Ctrl+C 停止监控并平仓")
            
            try:
                self.monitor_positions()
            except KeyboardInterrupt:
                print(f"[{datetime.now()}] 收到停止信号")
            
            # 6. 平仓
            self.close_positions()
            
            return True
            
        except Exception as e:
            print(f"[{datetime.now()}] 策略运行出错: {e}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            self.running = False
            try:
                self.api.close()
                print(f"[{datetime.now()}] API连接已关闭")
            except Exception as e:
                print(f"[{datetime.now()}] 关闭API连接失败: {e}")

def test_option_api():
    """测试期权 API 是否正常工作"""
    print("="*60)
    print("测试期权 API")
    print("="*60)
    
    try:
        from tqsdk import TqApi, TqAuth, TqSim
        api = TqApi(TqSim(), auth=TqAuth("lightdante", "Pk57485748"))
        
        # 测试查询沪深300期权
        print("查询沪深300期权合约...")
        try:
            options = api.query_options("SSE.000300")
            print(f"找到 {len(options)} 个沪深300期权合约")
            if options:
                print("示例合约:")
                for opt in options[:5]:
                    print(f"  - {opt}")
        except Exception as e:
            print(f"查询沪深300期权失败: {e}")
        
        # 测试查询中证500期权
        print("\n查询中证500期权合约...")
        try:
            options = api.query_options("SSE.000905")
            print(f"找到 {len(options)} 个中证500期权合约")
            if options:
                print("示例合约:")
                for opt in options[:5]:
                    print(f"  - {opt}")
        except Exception as e:
            print(f"查询中证500期权失败: {e}")
        
        api.close()
        print("\nAPI 测试完成")
    except Exception as e:
        print(f"测试失败: {e}")
    
    print("="*60)

if __name__ == "__main__":
    print("="*60)
    print("中证1000期权日历价差策略demo")
    print("="*60)
    print("策略说明:")
    print("1. 卖出3月到期的中证1000期权")
    print("2. 买入6月到期的中证1000期权")
    print("3. 利用时间价值衰减速度不同获利")
    print("="*60)
    
    # 先测试 API
    test_option_api()
    
    # 运行策略
    print("\n运行中证1000期权日历价差策略...")
    strategy = CSI1000OptionCalendarSpread()
    strategy.run_strategy()
    
    print("\n" + "="*60)
    print("策略执行完成")
    print("="*60)
