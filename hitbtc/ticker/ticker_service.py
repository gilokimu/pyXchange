from uplink import Consumer, get

from hitbtc.base.decorators import raise_for_status
from hitbtc.ticker.ticker_schema import TickerSchema


@raise_for_status
class TickerService(Consumer):
    """
        Hitbtc client
    """
    base_url = "https://api.hitbtc.com/api/2/"

    def __init__(self, public_key="", secret="", public=True):
        super(TickerService, self).__init__(base_url=self.base_url)
        if not public:
            self.session.auth = (public_key, secret)

    @get("public/ticker/{symbol_code}")
    def get_ticker(self, symbol_code) -> TickerSchema():
        """
        :param symbol_code: Symbol (currency pair) identifier, for example,
        ''ETHBTC''

        :returns returns a ticker identified with symbol code / currency pair
        """
        pass

    @get("public/ticker")
    def get_tickers(self) -> TickerSchema(many=True):
        """
        :returns list of all tickers
        """
        pass


def main():
    """
        Test of the hitbtc client
    """

    api = TickerService()


if __name__ == "__main__":
    main()
