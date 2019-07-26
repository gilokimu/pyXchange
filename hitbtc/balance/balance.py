import decimal


class Balance:
    """
        Trading balance
        currency: String: Currency code
        available: Number: Amount available for trading or transfer to main
        balance
        reserved: Number: Amount reserved for active orders or incomplete
        transfers to main balance
    """

    currency: str = None
    available: decimal = None
    reserved: decimal = None

    def __init__(self, currency=None, available=None, reserved=None):
        self.currency = currency
        self.available = available
        self.reserved = reserved

    def __str__(self) -> str:
        return self.__dict__.__str__()
