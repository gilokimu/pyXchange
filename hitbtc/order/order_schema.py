import datetime
import decimal

import marshmallow

from hitbtc.order.order import Order
from hitbtc.base.base_schema import SchemaBase


class OrderSchema(SchemaBase):
    """
        Serializes the symbol class
    """

    id: str = marshmallow.fields.Str()
    clientOrderId: decimal = marshmallow.fields.Str()
    symbol: decimal = marshmallow.fields.Str()
    side: str = marshmallow.fields.Str()
    type: decimal = marshmallow.fields.Str()
    timeInForce: decimal = marshmallow.fields.Str()
    quantity: str = marshmallow.fields.Decimal()
    price: decimal = marshmallow.fields.Decimal()
    stopPrice: decimal = marshmallow.fields.Decimal()
    expireTime: datetime = marshmallow.fields.DateTime()
    strictValidate: decimal = marshmallow.fields.Bool()
    postOnly: decimal = marshmallow.fields.Bool()

    createdAt: datetime = marshmallow.fields.DateTime()
    updatedAt: datetime = marshmallow.fields.DateTime()

    status: str = marshmallow.fields.Str()
    cummQuantity: str = marshmallow.fields.Str()

    @marshmallow.post_load
    def make_order(self, data) -> Order:
        """
        :param data: receives symbol data from api as json
        :return: returns Symbol python object
        """

        self.data = data

        return Order(id=self.get('id'),
                     client_order_id=self.get('clientOrderId'),
                     symbol=self.get('symbol'),
                     side=self.get('side'),
                     status=self.get('status'),
                     type=self.get('type'),
                     time_in_force=self.get('timeInForce'),
                     quantity=self.get('quantity'),
                     price=self.get('price'),
                     cumulative_quantity=self.get('cumQuantity'),
                     created_at=self.get('createdAt'),
                     updated_at=self.get('updatedAt'),
                     stop_price=self.get('stopPrice'),
                     post_only=self.get('postOnly'),
                     expire_time=self.get('expireTime'))
