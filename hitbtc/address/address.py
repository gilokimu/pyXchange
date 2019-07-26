class Address:
    """
        Data class for address
        :param address Address for deposit
        :param payment_id Optional parameter If this parameter is set,
        it is required for deposit.

    """

    address: str = None
    payment_id: str = None

    def __init__(self, address, payment_id):
        self.address = address
        self.payment_id = payment_id
