import os

from dotenv import load_dotenv
from uplink import Consumer, QueryMap, get

from hitbtc.base.decorators import raise_for_status
from hitbtc.trade.trade_schema import \
    TradeSchema

load_dotenv()


@raise_for_status
class TradeService(Consumer):
    """
        Hitbtc client
    """
    base_url = "https://api.hitbtc.com/api/2/"

    def __init__(self, api_key="", secret_key=""):
        super(TradeService, self).__init__(base_url=self.base_url)
        self.session.auth = (api_key, secret_key)

    @get("history/trades/")
    def trades(self, **params: QueryMap) -> TradeSchema(many=True):
        """
        :returns Gets historical trades as a list
        """
        pass

    @get("history/order/{order_id}/trades/")
    def order_trades(self, order_id, **params: QueryMap) -> \
            TradeSchema(
                    many=True):
        """
        :returns Get historical trades by specified order
        """
        pass


def main():
    """
        Test of the hitbtc client
    """

    api_key = os.getenv("HITBTC_API_KEY", "API_KEY")
    secret_key = os.getenv("HITBTC_SECRET_KEY", "SECRET KEY")

    api = TradeService(
            api_key=api_key,
            secret_key=secret_key,
    )

    for trade in api.trades():
        print(trade)


if __name__ == "__main__":
    main()
