import decimal

import marshmallow

from hitbtc.ticker.Ticker import Ticker
from hitbtc.base.base_schema import SchemaBase


class TickerSchema(SchemaBase):
    """
        Serializes the ticker class
    """

    ask: decimal = marshmallow.fields.Decimal()
    bid: decimal = marshmallow.fields.Decimal()
    last: decimal = marshmallow.fields.Decimal()
    open: decimal = marshmallow.fields.Decimal()
    low: decimal = marshmallow.fields.Decimal()
    high: decimal = marshmallow.fields.Decimal()
    volume: decimal = marshmallow.fields.Decimal()
    volumeQuote: decimal = marshmallow.fields.Decimal()
    timestamp: bool = marshmallow.fields.DateTime()
    symbol: str = marshmallow.fields.Str()

    @marshmallow.post_load
    def make_ticker(self, data) -> Ticker:
        """
        :param data: receives symbol data from api as json
        :return: returns Ticker object
        """

        self.data = data

        return Ticker(ask=self.get('ask'),
                      bid=self.get('bid'),
                      last=self.get('last'),
                      open=self.get('open'),
                      low=self.get('lpw'),
                      high=self.get('high'),
                      volume=self.get('volume'),
                      volume_quote=self.get('volumeQuote'),
                      timestamp=self.get('timestamp'),
                      symbol=self.get('symbol'))
