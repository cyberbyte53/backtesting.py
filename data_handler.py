import pandas as pd

def read_file(filename):
    return pd.read_csv(filename, index_col=0, parse_dates=True, infer_datetime_format=True)

def get_data(timeframe):
    valid_timeframes = ["3m","5m","15m","30m","1h"]
    assert timeframe in valid_timeframes, f"'{timeframe}' is not a valid timeframe. Choose from {valid_timeframes}."
    return read_file("Data/microbtcusdt_" + timeframe + ".csv")
