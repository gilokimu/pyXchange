"""
    Entity class for Candles data
    Candles are used for representation of a specific symbol as OHLC chart.
"""
import datetime
import decimal


class Candle:
    """
        Entity class for Candles data
    """

    def __init__(self, timestamp: datetime, open: decimal, close: decimal,
                 min: decimal, max: decimal, volume: decimal,
                 volume_quote: decimal):
        self.timestamp = timestamp
        self.open = open
        self.close = close
        self.min = min
        self.max = max
        self.volume = volume
        self.volume_quote = volume_quote

    def __str__(self) -> str:
        return self.__dict__.__str__()
