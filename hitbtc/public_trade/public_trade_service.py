import os

from dotenv import load_dotenv
from uplink import Consumer, QueryMap, get

from hitbtc.base.decorators import raise_for_status
from hitbtc.public_trade.public_trade_schema import PublicTradeSchema

load_dotenv()


@raise_for_status
class PublicTradeService(Consumer):
    """
        Hitbtc client
    """
    base_url = "https://api.hitbtc.com/api/2/"

    def __init__(self, api_key="", secret_key="", public=True):
        super(PublicTradeService, self).__init__(base_url=self.base_url)
        if not public:
            self.session.auth = (api_key, secret_key)

    @get("public/trades/{symbol_code}")
    def get_trades(self, symbol_code, **params: QueryMap) -> PublicTradeSchema(
            many=True):
        """
        :returns list of all tickers
        """
        pass


def main():
    """
        Test of the hitbtc client
    """

    api_key = os.getenv("HITBTC_API_KEY", "API_KEY")
    secret_key = os.getenv("HITBTC_SECRET_KEY", "SECRET KEY")

    api = PublicTradeService(api_key=api_key,
                             secret_key=secret_key,
                             public=False
                             )


if __name__ == "__main__":
    main()
