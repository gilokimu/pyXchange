import os
from pprint import pprint

from dotenv import load_dotenv
from uplink import Body, Consumer, QueryMap, delete, get, patch, post

from hitbtc.base.decorators import raise_for_status
from hitbtc.order.order_schema import OrderSchema

load_dotenv()


@raise_for_status
class OrderService(Consumer):
    """
        Order service
    """
    base_url = "https://api.hitbtc.com/api/2/"

    def __init__(self, api_key="", secret_key="", public=True):
        super(OrderService, self).__init__(base_url=self.base_url)
        if not public:
            self.session.auth = (api_key, secret_key)

    @get("order")
    def orders(self) -> OrderSchema(many=True):
        """
        :returns Return array of active orders.
        """

    @get("history/order")
    def historical_orders(self, **params: QueryMap) -> OrderSchema(many=True):
        """
        :returns Get historical orders
        """

    @get("order/{order_id}")
    def order(self, order_id) -> OrderSchema():
        """
        :returns Return order with order_id
        """

    @patch("order/{order_id}")
    def update_order(self, order_id) -> OrderSchema():
        """
        :returns Return array of active orders.
        """

    @post("order")
    def create_order(self, order: Body):
        """
        :param order: order body object to create
        """
        pass

    @delete("order/{symbol}")
    def cancel_orders(self, symbol):
        """
        Cancels all open orders
        :param symbol: symbol to filter orders that need to be cancelled
        """
        pass


def main():
    """
        Test of the hitbtc client
    """

    api_key = os.getenv("HITBTC_API_KEY", "API_KEY")
    secret_key = os.getenv("HITBTC_SECRET_KEY", "SECRET KEY")

    api = OrderService(api_key=api_key,
                       secret_key=secret_key,
                       public=False
                       )

    order = api.historical_orders(**{'side': 'buy'})
    pprint(order)


if __name__ == "__main__":
    main()
