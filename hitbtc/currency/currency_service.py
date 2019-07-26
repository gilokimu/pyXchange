from uplink import Consumer, get

from hitbtc.base.decorators import raise_for_status
from hitbtc.base.exceptions import TradeException
from hitbtc.currency.currency_schema import CurrencySchema


@raise_for_status
class CurrencyService(Consumer):
    """
        Hitbtc client
    """
    base_url = "https://api.hitbtc.com/api/2/"

    def __init__(self, public_key="", secret="", public=True):
        super(CurrencyService, self).__init__(base_url=self.base_url)
        if not public:
            self.session.auth = (public_key, secret)

    @get("public/currency/{currency_code}")
    def currency(self, currency_code) -> CurrencySchema():
        """
        :param currency_code: string representation of the currency
        :returns
        """
        pass

    @get("public/currency")
    def currencies(self) -> CurrencySchema(many=True):
        """
        :returns list of currencies
        """
        pass


def main():
    """
        Test of the hitbtc client
    """

    api = CurrencyService()

    try:
        print(api.currency("1254"))
    except TradeException as ex:
        print(ex)


if __name__ == "__main__":
    main()
