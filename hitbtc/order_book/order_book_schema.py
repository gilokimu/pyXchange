import marshmallow

from hitbtc.order_book.order_book import OrderBook, OrderBookItem
from hitbtc.base.base_schema import SchemaBase


class OrderBookItemSchema(SchemaBase):
    """
        Serializes the order book item data class
    """

    size = marshmallow.fields.Decimal()
    price = marshmallow.fields.Decimal()

    @marshmallow.post_load
    def make_order_book_item(self, data) -> OrderBookItem:
        """
        :param data: receives symbol data from api as json
        :return: returns Ticker object
        """

        self.data = data

        return OrderBookItem(size=self.get('size'),
                             price=self.get('price'))


class OrderBookSchema(SchemaBase):
    """
        Serializes the order book data class
    """

    ask = OrderBookItemSchema(many=True)
    bid = OrderBookItemSchema(many=True)
    timestamp = marshmallow.fields.DateTime()

    @marshmallow.post_load
    def make_order_book(self, data) -> OrderBook:
        """
        :param data: receives symbol data from api as json
        :return: returns Ticker object
        """

        self.data = data

        return OrderBook(ask=self.ask,
                         bid=self.bid,
                         timestamp=self.get('timestamp'))
