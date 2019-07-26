import marshmallow

from hitbtc.symbol.symbol import Symbol
from hitbtc.base.base_schema import SchemaBase


class SymbolSchema(SchemaBase):
    """
        Serializes the symbol class
    """

    id = marshmallow.fields.Str()
    baseCurrency = marshmallow.fields.Str()
    quoteCurrency = marshmallow.fields.Str()
    quantityIncrement = marshmallow.fields.Decimal()
    tickSize = marshmallow.fields.Decimal()
    takeLiquidityRate = marshmallow.fields.Decimal()
    provideLiquidityRate = marshmallow.fields.Decimal()
    feeCurrency = marshmallow.fields.Str()

    @marshmallow.post_load
    def make_symbol(self, data):
        """
        :param data: receives symbol data from api as json
        :return: returns Symbol python object
        """

        self.data = data

        return Symbol(id=self.get('id'),
                      base_currency=self.get('baseCurrency'),
                      quote_currency=self.get('quoteCurrency'),
                      quantity_increment=self.get('quantityIncrement'),
                      tick_size=self.get('tickSize'),
                      take_liquidity_rate=self.get('takeLiquidityRate'),
                      provide_liquidity_rate=self.get('provideLiquidityRate'),
                      fee_currency=self.get('feeCurrency'))
