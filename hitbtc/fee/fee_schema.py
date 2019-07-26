import decimal

import marshmallow

from hitbtc.fee.fee import Fee
from hitbtc.base.base_schema import SchemaBase


class FeeSchema(SchemaBase):
    """
        Serializes the fee data class
    """

    takeLiquidityRate: decimal = marshmallow.fields.Decimal()
    provideLiquidityRate: decimal = marshmallow.fields.Decimal()

    @marshmallow.post_load
    def make_fee(self, data) -> Fee:
        """
        :param data: receives symbol data from api as json
        :return: returns Fee python object
        """

        self.data = data

        return Fee(
                take_liquidity_rate=self.get('takeLiquidityRate'),
                provide_liquidity_rate=self.get('provideLiquidityRate'))
