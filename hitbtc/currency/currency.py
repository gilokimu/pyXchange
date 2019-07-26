import decimal


class Currency:
    """
        Get list of avialable Symbols (Currency Pairs). You can read more
        info at http://www.investopedia.com/terms/c/currencypair.asp
    """
    id: str = None
    full_name: str = None
    crypto: bool = None
    payin_enabled: bool = None
    payin_payment_id: bool = None
    payin_confirmations: int = None
    payout_enabled: bool = None
    payout_is_payment_id: bool = None
    transfer_enabled: bool = None
    delisted: bool = None
    payout_fee: decimal = None

    def __init__(self, id: str = None, full_name: str = None,
                 crypto: bool = None, payin_enabled: bool = None,
                 payin_payment_id: bool = None,
                 payin_confirmations: int = None, payout_enabled: bool = None,
                 payout_is_payment_id: bool = None,
                 transfer_enabled: bool = None, delisted: bool = None,
                 payout_fee: decimal = None):
        self.id: str = id
        self.full_name: str = full_name
        self.crypto: bool = crypto
        self.payin_enabled: bool = payin_enabled
        self.payin_payment_id: bool = payin_payment_id
        self.payin_confirmations: int = payin_confirmations
        self.payout_enabled: bool = payout_enabled
        self.payout_is_payment_id: bool = payout_is_payment_id
        self.transfer_enabled: bool = transfer_enabled
        self.delisted: bool = delisted
        self.payout_fee: decimal = payout_fee

    def __str__(self) -> str:
        return self.__dict__.__str__()

    def to_dictionary(self):
        """
        Converts entity to dictionary with non nun values
        :return:
        """
        currency_dict = {}
        for key in self.__dict__:
            value = self.__dict__[key]
            if value:
                currency_dict[key] = value

        return currency_dict


