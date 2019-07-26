import decimal
from enum import Enum


class Status:
    """
        Object state
    """

    def __init__(self, status: str):
        self.status: str = status

    def get_status(self) -> str:
        """
        :return: object state string
        """
        return self.status


class TimeInForce:
    """
        Time in Force is a special instruction used when placing a order to
        indicate how long an order will remain active before it is executed
        or expired
    """

    def __init__(self, time_in_force: str):
        self.time_in_force: str = time_in_force

    def get_time_in_force(self) -> str:
        """
        :return: object state string
        """
        return self.time_in_force


class Type:
    """
        Order type
    """

    def __init__(self, type: str):
        self.type: str = type

    def get_type(self) -> str:
        """
        :return: object state string
        """
        return self.type


class Side:
    """
        Order side
    """

    def __init__(self, side: str):
        self.side: str = side

    def get_side(self) -> str:
        """
        :return: object state string
        """
        return self.side


class OrderTimeInForce(Enum):
    """
        Order side enum
    """

    GTC = Side("GTC")
    IOC = Side("IOC")
    FOK = Side("FOK")
    Day = Side("Day")
    GTD = Side("GTD")


class OrderSide(Enum):
    """
        Order side enum
    """

    SELL = Side("sell")
    BUY = Side("buy")


class OrderType(Enum):
    """
        Order side enum
    """

    LIMIT = Type("limit")
    MARKET = Type("public_trade")
    STOP_LIMIT = Type("stopLimit")
    STOP_MARKET = Type("stopMarket")


class OrderStatus(Enum):
    """
        Order state
    """

    NEW = Status("new")
    SUSPENDED = Status("new")
    PARTIALLY_FILLED = Status("new")
    FILLED = Status("new")
    CANCELLED = Status("new")
    EXPIRED = Status("new")


class Order:
    """
        Order class

        Arg
        :id -Order unique identifier as assigned by exchange

        :clientOrderId- Order unique identifier as assigned by trader.

        :Uniqueness must be guaranteed within a single trading day, including
        all

        :active orders.

        :symbol	String	Trading symbol name

        :side	String	Trade side. Accepted values: sell or buy

        :status	String	Order state Accepted values: new, suspended,
        partiallyFilled, filled, canceled, expired

        :type	String	Accepted values: limit, public_trade, stopLimit, stopMarket

        :timeInForce String	Time in Force is a special instruction used
        when placing a order to indicate how long an order will remain active
        before it is executed or expired.

            GTC - ''Good-Till-Cancelled'' order won't be closed until it is
            filled.

            IOC - ''Immediate-Or-Cancel'' order must be executed immediately.
            Any part of an IOC order that cannot be filled immediately will
            be cancelled.

            FOK - ''Fill-Or-Kill'' is a type of ''Time in Force'' designation
            used in securities trading that instructs a brokerage to execute
            a transaction immediately and completely or not execute it at all.

            Day - keeps the order active until the end of the trading day (UTC).

            GTD - ''Good-Till-Date''. The date is specified in expireTime.

        :quantity	Number	Order quantity

        :price	Number	Order price

        :cumQuantity	Number	Cumulative executed quantity

        :createdAt	Datetime	The date when order has been created

        :updatedAt	Datetime	The date of order last update

        :stopPrice	Number	Required for stop-limit orders

        :postOnly	Boolean	A post-only order is an order that does not
        remove liquidity. If your post-only order causes a match with a
        pre-existing order as a taker, then order will be cancelled.
        expireTime	Datetime	Date of order expiration for timeInForce = GTD
    """

    id = None
    client_order_id = None
    symbol = None
    side: Side = None
    status: Status = None
    type: Type = None
    time_in_force = None
    quantity = None
    price = None
    cumulative_quantity = None
    created_at = None
    updated_at = None
    stop_price = None
    post_only = None
    expire_time = None

    def __init__(self, id=None, client_order_id=None, symbol=None, side=None,
                 status=None, type=None, time_in_force=None, quantity=None,
                 price=None, cumulative_quantity=None, created_at=None,
                 updated_at=None, stop_price=None, post_only=None,
                 expire_time=None):
        self.id = id
        self.client_order_id = client_order_id
        self.symbol = symbol
        self.side = side
        self.status = status
        self.type = type
        self.time_in_force = time_in_force
        self.quantity: decimal = quantity
        self.price:decimal = price
        self.cumulative_quantity = cumulative_quantity
        self.created_at = created_at
        self.updated_at = updated_at
        self.stop_price = stop_price
        self.post_only = post_only
        self.expire_time = expire_time

    def total(self) -> decimal:
        """
        :returns the total as a product pf price and quantity
        """
        return round(self.quantity * self.price, 2)

    class Builder:
        """
            Builder for orders
        """

        def __init__(self):
            self.order = Order()

        def with_client_order_id(self, client_order_id: str):
            """
            :param client_order_id: Optional parameter If it is skipped,
            it will be generated by Server. Uniqueness must be guaranteed
            within a single trading day, including all active orders.
            """
            self.order.client_order_id = client_order_id
            return self

        def with_symbol(self, symbol: str):
            """
            :param symbol: Trading symbol
            """
            self.order.symbol = symbol
            return self

        def with_side(self, side: Side):
            """
            :param side: Trade side : Accepted values: OrderSide.SELL or
            OrderSide.SELL
            """
            self.order.side = side.get_side()
            return self

        def with_type(self, type: Type = OrderType.LIMIT):
            """
            :param type: Optional parameter Accepted values: OrderType.LIMIT,
            OrderType.MARKET, OrderType.STOP_LIMIT, OrderType.STOP_MARKET
            Default value: OrderType.LIMIT
            """
            self.order.type = type.get_type()
            return self

        def with_time_in_force(self, time_in_force: TimeInForce):
            """
            :param time_in_force: Optional parameter Accepted values: GTC,
            IOC, FOK, Day, GTD Default value: GDC
            """
            self.order.time_in_force = time_in_force.get_time_in_force()
            return self

        def with_quantity(self, quantity: decimal):
            """
                :param quantity: Order quantity
            """

            self.order.quantity = quantity
            return self

        def with_price(self, price: decimal):
            """
                :param price: Order quantity
            """

            self.order.price = price
            return self

        def with_stop_price(self, stop_price: decimal):
            """
                :param stop_price: Required for stop-limit orders
            """

            self.order.stop_price = stop_price
            return self

        def with_expire_time(self, expire_time: decimal):
            """
                :param expire_time: Required for orders with timeInForce = GTD
            """

            self.order.expire_time = expire_time
            return self

        def with_strict_validate(self, strict_validate: bool):
            """
                :param strict_validate: Price and quantity will be checked
                for the incrementation within tick size and quantity step.
                See symbol's tickSize and quantityIncrement.
            """

            self.order.strict_validate = strict_validate
            return self

        def with_post_only(self, post_only: bool):
            """
                :param post_only: A post-only order is an order that does not
                remove liquidity. If your post-only order causes a match with
                a pre-existing order as a taker, then order will be cancelled.
            """

            self.order.post_only = post_only
            return self

        def build(self):
            """
                :returns a dictionary of order dict with set values
            """
            order_dict = {}

            for key in self.order.__dict__.keys():
                if self.order.__dict__[key] is not None:
                    order_dict[key] = self.order.__dict__[key]

            return order_dict

    def __str__(self) -> str:
        return self.__dict__.__str__()

    def to_dictionary(self):
        """
        converts to dictionary
        :return: dict representation of order
        """
        order_dict = {}
        for key in self.__dict__:
            value = self.__dict__[key]
            if value:
                order_dict[key] = value

        return order_dict
