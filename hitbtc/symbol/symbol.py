import decimal


class Symbol:
    """
        Entity file for a symbol (Currency pair) is the quotation of two
        different currencies, with the value of one currency being quoted
        against the other

        :param id Symbol (currency pair) identifier, for example, ''ETHBTC''
        Note: description will simply use symbol in the future.

        :param base_currency : Name (code) of base currency, for example,
        ''ETH''

        :param quote_currency : Name of quote currency

        :param quantity_increment : Symbol quantity should be divided by this
        value
        without residue


    """

    id: str = None
    base_currency: str = None
    quote_currency: str = None
    quantity_increment: decimal = None
    tick_size: decimal = None
    take_liquidity_rate: decimal = None
    provide_liquidity_rate: decimal = None
    fee_currency: str = None

    def __init__(self, id=None, base_currency=None, quote_currency=None,
                 quantity_increment=None, tick_size=None,
                 take_liquidity_rate=None, provide_liquidity_rate=None,
                 fee_currency=None):
        self.id = id
        self.base_currency = base_currency
        self.quote_currency = quote_currency
        self.quantity_increment = quantity_increment
        self.tick_size = tick_size
        self.take_liquidity_rate = take_liquidity_rate
        self.provide_liquidity_rate = provide_liquidity_rate
        self.fee_currency = fee_currency

    def __str__(self) -> str:
        return self.__dict__.__str__()
