import datetime
import decimal


class Ticker:
    """
        Entity class for Candles data
    """

    ask: decimal = None
    bid: decimal = None
    last: decimal = None
    open: decimal = None
    low: decimal = None
    high: decimal = None
    volume: decimal = None
    volume_quote: decimal = None
    timestamp: datetime = None
    symbol: str = None

    def __init__(self, ask: decimal = None,
                 bid: decimal = None,
                 last: decimal = None,
                 open: decimal = None,
                 low: decimal = None,
                 high: decimal = None,
                 volume: decimal = None,
                 volume_quote: decimal = None,
                 timestamp: datetime = None,
                 symbol: str = None):
        self.ask: decimal = ask
        self.bid: decimal = bid
        self.last: decimal = last
        self.open: decimal = open
        self.low: decimal = low
        self.high: decimal = high
        self.volume: decimal = volume
        self.volume_quote: decimal = volume_quote
        self.timestamp: datetime = timestamp
        self.symbol: str = symbol

    def __str__(self) -> str:
        return self.__dict__.__str__()
