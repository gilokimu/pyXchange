"""
    Entity class for Transaction data
"""
import datetime
import decimal


class Transaction:
    """
    Holds the transaction data fields

    Args:
        id:	String	Transaction unique identifier as assigned by exchange
        index:	Number	Is the internal index value that represents when the
            entry was updated
        currency:	String	Currency code
        amount:	Number	Amount of traded currency
        fee:	Number	Payment commission value
        address:	String	Address identifier
        payment_id:	String	Optional parameter
        hash:	String	Transaction hash
        status:	String	Accepted values: created, pending, failed, success
        type:	String	Accepted values: payout (crypto withdraw transaction),
            payin (crypto deposit transaction), deposit, withdraw,
            bankToExchange, exchangeToBank
        created_at:	Datetime	The date when Transaction has been created
        updated_at:	Datetime	The date of Transaction last update
    """

    id: str
    index: int
    currency: str
    amount: decimal
    fee: decimal
    address: str
    payment_id: str
    hash: str
    status: str
    type: str
    created_at: datetime
    updated_at: datetime

    def __init__(self,
                 id: str = None,
                 index: int = None,
                 currency: str = None,
                 amount: decimal = None,
                 fee: decimal = None,
                 address: str = None,
                 payment_id: str = None,
                 hash: str = None,
                 status: str = None,
                 type: str = None,
                 created_at: datetime = None,
                 updated_at: datetime = None
                 ):
        """
            Holds the transaction data fields

            Args:
                id:	(String)	Transaction unique identifier as assigned by
                    exchange
                index:	(Number)	Is the internal index value that represents
                when the entry was updated
                currency:	(String)	Currency code
                amount:	(Number)	Amount of traded currency
                fee:	(Number)	Payment commission value
                address:	(String) Address identifier
                payment_id:	(String) Optional parameter
                hash:	(String) Transaction hash
                status:	(String) Accepted values: created, pending, failed,
                    success
                type:	(String) Accepted values: payout (crypto withdraw
                transaction), payin (crypto deposit transaction), deposit,
                withdraw, bankToExchange, exchangeToBank
                created_at:	(Datetime) - The date when Transaction has been
                    created
                updated_at:	(Datetime) The date of Transaction last update
            """
        self.id: str = id
        self.index: int = index
        self.currency: str = currency
        self.amount: decimal = amount
        self.fee: decimal = fee
        self.address: str = address
        self.payment_id: str = payment_id
        self.hash: str = hash
        self.status: str = status
        self.type: str = type
        self.created_at: datetime = created_at
        self.updated_at: datetime = updated_at

    def __str__(self) -> str:
        return self.__dict__.__str__()
