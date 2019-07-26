import datetime
import decimal
from typing import List


class OrderBookItem:
    """
    :param size	: Number: Total volume of orders with the specified price
    :param price : Number Price level
    """

    size: decimal = None
    price: decimal = None

    def __init__(self, size: decimal = None, price: decimal = None):
        self.size = size
        self.price = price

    def __str__(self) -> str:
        return self.__dict__.__str__()


class OrderBook:
    """
        An Order Book is an electronic list of buy and sell orders for a
        specific symbol, structured by price level.

        :param ask	Array	Ask side array of levels
        :param bid	Array	Bid side array of levels
        :param timestamp	Number	Total volume of orders with the specified
        price
    """

    ask: List[OrderBookItem] = None
    bid: List[OrderBookItem] = None
    timestamp: List[OrderBookItem] = None

    def __init__(self, ask: List[OrderBookItem], bid: List[OrderBookItem],
                 timestamp: timestamp):
        self.ask = ask
        self.bid = bid
        self.timestamp = timestamp

    def __str__(self) -> str:
        return self.__dict__.__str__()
