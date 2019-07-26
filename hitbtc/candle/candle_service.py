from uplink import Consumer, QueryMap, get

from hitbtc.base.decorators import raise_for_status
from hitbtc.candle.candle_schema import CandleSchema


@raise_for_status
class CandleService(Consumer):
    """
        Hitbtc clientpip
    """
    base_url = "https://api.hitbtc.com/api/2/"

    def __init__(self, public_key="", secret="", public=True):
        super(CandleService, self).__init__(base_url=self.base_url)
        if not public:
            self.session.auth = (public_key, secret)

    @get("public/candles/{symbol_code}")
    def get_candles(self, symbol_code, **params: QueryMap) -> CandleSchema(
            many=True):
        """
        :returns list of all tickers
        """
        pass


def main():
    """
        Test of the hitbtc client
    """

    api = CandleService()
    for candle in api.get_candles("ETHBTC"):
        print(candle)


if __name__ == "__main__":
    main()
