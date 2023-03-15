from hummingbot.strategy.script_strategy_base import ScriptStrategyBase


class QuickstartScript(ScriptStrategyBase):

    # It is best to first use a paper trade exchange connector 
    # while coding your strategy, once you are happy with it
    # then switch to real one.

    markets = { 
            "binance_paper_trade": {"BTC-USDT"}, 
            "kucoin_paper_trade": {"ETH-USDT"}
            }

    def on_tick(self):
      btc_price = self.connectors["binance_paper_trade"].get_mid_price("BTC-USDT")
      eth_price = self.connectors["kucoin_paper_trade"].get_mid_price("ETH-USDT")
      btc_msg = f"Bitcoin price: ${btc_price}"
      eth_msg = f"ETH price: ${eth_price}"
      self.logger().info(btc_msg)
      self.logger().info(eth_msg)
      self.notify_hb_app_with_timestamp(btc_msg)
      self.notify_hb_app_with_timestamp(eth_msg)