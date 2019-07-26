from uplink import Consumer, get

from hitbtc.base.decorators import raise_for_status
from hitbtc.symbol.symbol_schema import SymbolSchema


@raise_for_status
class SymbolService(Consumer):
    """
        Hitbtc client
    """
    base_url = "https://api.hitbtc.com/api/2/"

    def __init__(self, public_key="", secret="", public=True):
        super(SymbolService, self).__init__(base_url=self.base_url)
        if not public:
            self.session.auth = (public_key, secret)

    @get("public/symbol/{symbol_code}")
    def get_symbol(self, symbol_code) -> SymbolSchema():
        """
        :param symbol_code: Symbol (currency pair) identifier, for example,
        ''ETHBTC''

        :returns Returns the currency symbols (currency pair)
        traded on exchange with the symbol code provide in the parameter.
        The first listed currency of a symbol is called the base currency, and
        the second currency is called the quote currency. The currency pair
        indicates how much of the quote currency is needed to purchase one
        unit of the base currency
        """
        pass

    @get("public/symbol")
    def get_symbols(self) -> SymbolSchema(many=True):
        """
        :param

        :returns Return the actual list of currency symbols (currency pairs)
        traded on exchange. The first listed currency of a symbol is called
        the base currency, and the second currency is called the quote
        currency. The currency pair indicates how much of the quote currency
        is needed to purchase one unit of the base currency

        """
        pass


def main():
    """
        Test of the hitbtc client
    """

    api = SymbolService()


if __name__ == "__main__":
    main()
