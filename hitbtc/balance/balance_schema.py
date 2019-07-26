import decimal

import marshmallow

from hitbtc.balance.balance import Balance
from hitbtc.base.base_schema import SchemaBase


class BalanceSchema(SchemaBase):
    """
        Serializes the symbol class
    """

    currency: str = marshmallow.fields.Str()
    available: decimal = marshmallow.fields.Decimal()
    reserved: decimal = marshmallow.fields.Bool()

    @marshmallow.post_load
    def make_balance(self, data) -> Balance:
        """
        :param data: receives symbol data from api as json
        :return: returns Symbol python object
        """

        self.data = data

        return Balance(currency=self.get('currency'),
                       available=self.get('available'),
                       reserved=self.get('reserved'))
