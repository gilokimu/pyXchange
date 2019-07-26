import datetime
import decimal

import marshmallow

from hitbtc.trade.historical_trade import Trade
from hitbtc.base.base_schema import SchemaBase


class TradeSchema(SchemaBase):
    """
        Serializes the order data class
    """

    id: int = marshmallow.fields.Int()
    clientOrderId: str = marshmallow.fields.Str()
    orderId: int = marshmallow.fields.Int()
    symbol: str = marshmallow.fields.Str()
    side: str = marshmallow.fields.Str()
    quantity: decimal = marshmallow.fields.Decimal()
    fee: decimal = marshmallow.fields.Decimal()
    price: decimal = marshmallow.fields.Decimal()
    timestamp: datetime = marshmallow.fields.DateTime()

    @marshmallow.post_load
    def make_historical_trade(self, data) -> Trade:
        """
        :param data: receives symbol data from api as json
        :return: returns Historical Trade object
        """

        self.data = data

        return Trade(id=self.get('id'),
                     client_order_id=self.get('clientOrderId'),
                     order_id=self.get('orderId'),
                     symbol=self.get('symbol'),
                     side=self.get('side'),
                     quantity=self.get('quantity'),
                     fee=self.get('fee'),
                     price=self.get('price'),
                     timestamp=self.get('timestamp')
                     )
