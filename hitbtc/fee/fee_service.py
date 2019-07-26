from uplink import Consumer, get

from hitbtc.base.decorators import raise_for_status
from hitbtc.fee.fee_schema import FeeSchema


@raise_for_status
class FeeService(Consumer):
    """
        Hitbtc client
    """
    base_url = "https://api.hitbtc.com/api/2/"

    def __init__(self, public_key="", secret="", public=True):
        super(FeeService, self).__init__(base_url=self.base_url)
        if not public:
            self.session.auth = (public_key, secret)

    @get("public/trading/fee/{symbol_code}")
    def fee(self, symbol_code) -> FeeSchema():
        """
        :param symbol_code: Symbol (currency pair) identifier, for example,
        ''ETHBTC''

        :returns Get trading fee rate
        """
        pass


def main():
    """
        Test of the hitbtc client
    """

    api = FeeService()


if __name__ == "__main__":
    main()
