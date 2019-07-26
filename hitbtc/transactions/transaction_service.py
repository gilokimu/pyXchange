import os

from dotenv import load_dotenv
from uplink import Consumer, QueryMap, get

from hitbtc.base.decorators import raise_for_status
from hitbtc.transactions.transaction_schema import TransactionSchema

load_dotenv()


@raise_for_status
class TransactionService(Consumer):
    """
        Transaction API service
    """
    base_url = "https://api.hitbtc.com/api/2/"

    def __init__(self, api_key="", secret_key="", public=True):
        super(TransactionService, self).__init__(base_url=self.base_url)
        if not public:
            self.session.auth = (api_key, secret_key)

    @get("account/transactions")
    def get_transactions(self, **params: QueryMap) -> TransactionSchema(
            many=True):
        """
        :returns list of all transactions
        """
        pass

    @get("account/transactions/{transaction_id}")
    def get_transaction(self, transaction_id) -> TransactionSchema():
        """
        :param transaction_id the id of the transaction to get
        :returns transaction with specified transaction id
        :raises TradeException if no such transaction id
        """
        pass


def main():
    """
        Test of the hitbtc client
    """

    api_key = os.getenv("HITBTC_API_KEY", "API_KEY")
    secret_key = os.getenv("HITBTC_SECRET_KEY", "SECRET KEY")

    api = TransactionService(
            api_key=api_key,
            secret_key=secret_key,
            public=False
    )

    for transaction in api.get_transactions():
        print(transaction)

    transaction = api.get_transaction('da4d3d03-f322-4140-b07e-f7ab4a154dd1')
    print(transaction)


if __name__ == "__main__":
    main()
