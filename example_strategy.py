from backtesting.backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import pandas as pd
from data_handler import get_data


# timeframes = ["3m","5m","15m","30m","1h"]
data = get_data("1h")

class SmaCross(Strategy):
    def init(self):
        price = self.data.Close
        self.ma1 = self.I(SMA, price, 10)
        self.ma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.ma1, self.ma2):
            self.buy()
        elif crossover(self.ma2, self.ma1):
            self.sell()


bt = Backtest(data, SmaCross, commission=.001,
              exclusive_orders=False)
stats = bt.run()
print(stats)
bt.plot()