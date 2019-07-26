"""
    Serializes the public public_trade class
"""
import datetime
import decimal

import marshmallow

from hitbtc.public_trade.public_trade import PublicTrade
from hitbtc.base.base_schema import SchemaBase


class PublicTradeSchema(SchemaBase):
    """
        Serializes the public public_trade data class
    """

    id: int = marshmallow.fields.Decimal()
    price: decimal = marshmallow.fields.Decimal()
    quantity: int = marshmallow.fields.Decimal()
    side: str = marshmallow.fields.Decimal()
    timestamp: datetime = marshmallow.fields.DateTime()

    @marshmallow.post_load
    def make_trade(self, data) -> PublicTrade:
        """
        :param data: receives public public_trade data from api as json
        :return: returns public public_trade object
        """

        self.data = data

        return PublicTrade(id=self.get('id'),
                           price=self.get('price'),
                           quantity=self.get('quantity'),
                           side=self.get('side'),
                           timestamp=self.get('timestamp'),
                           )
