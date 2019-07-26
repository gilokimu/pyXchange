import datetime
import decimal

import marshmallow

from hitbtc.transactions.transaction import Transaction
from hitbtc.base.base_schema import SchemaBase


class TransactionSchema(SchemaBase):
    """
        Serializes the transaction data class
    """

    id: str = marshmallow.fields.Str()
    index: int = marshmallow.fields.Int()
    currency: str = marshmallow.fields.Str()
    amount: decimal = marshmallow.fields.Decimal()
    fee: decimal = marshmallow.fields.Decimal()
    address: str = marshmallow.fields.Str()
    paymentId: str = marshmallow.fields.Str()
    hash: str = marshmallow.fields.Str()
    status: str = marshmallow.fields.Str()
    type: str = marshmallow.fields.Str()
    createdAt: datetime = marshmallow.fields.DateTime()
    updatedAt: datetime = marshmallow.fields.DateTime()

    @marshmallow.post_load
    def make_transaction(self, data) -> Transaction:
        """
        :param data: receives symbol data from api as json
        :return: returns Transaction object
        """

        self.data = data

        return Transaction(
                id=self.get('id'),
                index=self.get('index'),
                currency=self.get('currency'),
                amount=self.get('amount'),
                fee=self.get('fee'),
                address=self.get('address'),
                payment_id=self.get('paymentId'),
                hash=self.get('hash'),
                status=self.get('status'),
                type=self.get('type'),
                created_at=self.get('createdAt'),
                updated_at=self.get('updatedAt')
        )
