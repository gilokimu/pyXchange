import datetime
import decimal

import marshmallow

from hitbtc.candle.candle import Candle
from hitbtc.base.base_schema import SchemaBase


class CandleSchema(SchemaBase):
    """
        Serializes the order data class
    """

    timestamp: datetime = marshmallow.fields.DateTime()
    open: decimal = marshmallow.fields.Decimal()
    close: decimal = marshmallow.fields.Decimal()
    min: decimal = marshmallow.fields.Decimal()
    max: decimal = marshmallow.fields.Decimal()
    volume: decimal = marshmallow.fields.Decimal()
    volumeQuote: decimal = marshmallow.fields.Decimal()

    @marshmallow.post_load
    def make_candle(self, data) -> Candle:
        """
        :param data: receives symbol data from api as json
        :return: returns Ticker object
        """

        self.data = data

        return Candle(
                      timestamp=self.get('timestamp'),
                      open=self.get('open'),
                      close=self.get('close'),
                      min=self.get('min'),
                      max=self.get('max'),
                      volume=self.get('volume'),
                      volume_quote=self.get('volumeQuote'))
