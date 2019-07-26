import os

from dotenv import load_dotenv
from uplink import Consumer, get

from hitbtc.balance.balance_schema import BalanceSchema
from hitbtc.base.decorators import raise_for_status

load_dotenv()


@raise_for_status
class BalanceService(Consumer):
    """
        Trade services
    """
    base_url = "https://api.hitbtc.com/api/2/"

    def __init__(self, api_key="", secret_key="", public=True):
        super(BalanceService, self).__init__(base_url=self.base_url)
        if not public:
            self.session.auth = (api_key, secret_key)

    @get("trading/balance")
    def trading_balance(self) -> BalanceSchema(many=True):
        """
        :returns list of balance objects containing
            :currency: String Currency code
            :available: Number: Amount available for trading or transfer to
            main balance
            :reserved: Number: Amount reserved for active orders or incomplete
            transfers to main balance
        """

    @get("balance/balance")
    def account_balance(self) -> BalanceSchema(many=True):
        """
        :returns list of balance objects containing
            :currency: String Currency code
            :available: Number: Amount available for trading or transfer to
            main balance
            :reserved: Number: Amount reserved for active orders or incomplete
            transfers to main balance
        """


def main():
    """
        Test of the hitbtc client
    """

    api_key = os.getenv("HITBTC_API_KEY", "API_KEY")
    secret_key = os.getenv("HITBTC_SECRET_KEY", "SECRET KEY")

    api = BalanceService(api_key=api_key,
                         secret_key=secret_key,
                         public=False
                         )

    print("Trading balance")

    for balance in api.trading_balance():
        if balance.available > 0:
            print(balance)

    print("Account balance")

    for balance in api.account_balance():
        if balance.available > 0:
            print(balance)


if __name__ == "__main__":
    main()
