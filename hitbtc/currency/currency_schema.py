import decimal

import marshmallow

from hitbtc.currency.currency import Currency
from hitbtc.base.base_schema import SchemaBase


class CurrencySchema(SchemaBase):
    """
        Serializes the symbol class
    """

    id: str = marshmallow.fields.Str()
    fullName: str = marshmallow.fields.Str()
    crypto: bool = marshmallow.fields.Bool()
    payinEnabled: bool = marshmallow.fields.Bool()
    payinPaymentId: bool = marshmallow.fields.Bool()
    payinConfirmations: int = marshmallow.fields.Int()
    payoutEnabled: bool = marshmallow.fields.Bool()
    payoutIsPaymentId: bool = marshmallow.fields.Bool()
    transferEnabled: bool = marshmallow.fields.Bool()
    delisted: bool = marshmallow.fields.Bool()
    payoutFee: decimal = marshmallow.fields.Decimal()

    @marshmallow.post_load
    def make_currency(self, data) -> Currency:
        """
        :param data: receives symbol data from api as json
        :return: returns Symbol python object
        """

        self.data = data

        return Currency(id=self.get('id'),
                        full_name=self.get('fullName'),
                        crypto=self.get('crypto'),
                        payin_enabled=self.get('payinEnabled'),
                        payin_payment_id=self.get('payinPaymentId'),
                        payin_confirmations=self.get('payinConfirmations'),
                        payout_enabled=self.get('payoutEnabled'),
                        payout_is_payment_id=self.get('payoutIsPaymentId'),
                        transfer_enabled=self.get('transferEnabled'),
                        delisted=self.get('delisted'),
                        payout_fee=self.get('payoutFee'))
