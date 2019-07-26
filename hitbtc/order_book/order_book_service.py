from uplink import Consumer, get

from hitbtc.base.decorators import raise_for_status
from hitbtc.order_book.order_book_schema import OrderBookSchema


@raise_for_status
class OrderBookService(Consumer):
    """
        Hitbtc client
    """
    base_url = "https://api.hitbtc.com/api/2/"

    def __init__(self, public_key="", secret="", public=True):
        super(OrderBookService, self).__init__(base_url=self.base_url)
        if not public:
            self.session.auth = (public_key, secret)

    @get("public/orderbook/{symbol_code}")
    def get_order_book(self, symbol_code) -> OrderBookSchema():
        """
        :returns  list of buy and sell orders for a specific symbol,
        structured by price level.
        """
        pass


def main():
    """
        Test of the hitbtc client
    """

    api = OrderBookService()


if __name__ == "__main__":
    main()
