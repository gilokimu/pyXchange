"""
    data class to hold public_trade data
"""
import datetime
import decimal


class Trade:
    """
        :param id (Number) Trade unique identifier as assigned by exchange
        :param order_id	(Number) Order unique identifier as assigned by
        exchange
        :param client_order_id (String) Order unique identifier as assigned
        by trader
        :param symbol (String) Trading symbol
        :param side	(String) Trade side. Accepted values are sell or buy
        :param quantity	(Number) Trade quantity
        :param price (Number) Trade price
        :param fee (Number) Trade commission. Can be negative (''rebate'' -
        reward paid to a trader). See fee currency in the symbol config.
        :param timestamp (Datetime) Trade timestamp

    """

    id: int
    client_order_id: str
    order_id: int
    symbol: str
    side: str
    quantity: decimal
    fee: decimal
    price: decimal
    timestamp: datetime

    def __init__(self, id: int = None,
                 client_order_id: str = None,
                 order_id: int = None,
                 symbol: str = None,
                 side: str = None,
                 quantity: decimal = None,
                 fee: decimal = None,
                 price: decimal = None,
                 timestamp: datetime = None):
        self.id: int = id
        self.client_order_id: str = client_order_id
        self.order_id: int = order_id
        self.symbol: str = symbol
        self.side: str = side
        self.quantity: decimal = quantity
        self.fee: decimal = fee
        self.price: decimal = price
        self.timestamp: datetime = timestamp

    def __str__(self) -> str:
        return self.__dict__.__str__()
