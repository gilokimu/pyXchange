import decimal


class Withdrawal:
    """
        :param currency	Currency code
        :param amount	The amount that will be sent to the specified address
        :param address	Address identifier
        :param payment_id Optional parameter
        :param network_fee	Optional parameter. Too low or too high commission
        value will be rounded to valid value.
        :param include_fee	Default value is false. If true is set,
        then total spent value will include fee and networkFee.
        :param auto_commit	Boolean	Default is true. If false is set,
        then you should commit or rollback transaction in an
        hour. Used in two phase commit schema.
    """

    currency: str = None
    amount: decimal = None
    address: str = None
    payment_id: str = None
    network_fee: decimal = None
    include_fee: bool = None
    auto_commit: bool = None

    def __init__(self, currency: str = None, amount: decimal = None,
                 address: str = None, payment_id: str = None,
                 network_fee: decimal = None, include_fee: bool = None,
                 auto_commit: bool = None):
        self.currency: str = currency
        self.amount: decimal = amount
        self.address: str = address
        self.payment_id: str = payment_id
        self.network_fee: decimal = network_fee
        self.include_fee: bool = include_fee
        self.auto_commit: bool = auto_commit
