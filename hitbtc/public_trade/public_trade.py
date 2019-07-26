import datetime
import decimal
from enum import Enum


class SortDirection(Enum):
    """
        Class to use to define sort direction
    """

    ASC = "ASC"
    DESC = "DESC"


class FilterBy(Enum):
    """
        Class to use to define criteria to use when filtering
    """

    ID = "id"
    TIMESTAMP = "timestamp"


class FilterDate(Enum):
    """
        Class to use to ease access to date
    """

    NOW = datetime.datetime.now()
    TODAY = datetime.datetime.today()
    YESTERDAY = datetime.datetime.today() - datetime.timedelta(days=1)
    LAST_WEEK = datetime.datetime.now()
    THIS_MONTH = datetime.datetime.now()
    LAST_MONTH = datetime.datetime.now()
    THIS_YEAR = datetime.datetime.now()


class PublicTrade:
    """
        Entity class for Trade data
    """

    id: int = None
    price: decimal = None
    quantity: decimal = None
    side: str = None
    timestamp: datetime = None

    def __init__(self, id=None, price=None, quantity=None, side=None,
                 timestamp=None
                 ):
        self.id: decimal = id
        self.price: decimal = price
        self.quantity: decimal = quantity
        self.side: decimal = side
        self.timestamp: decimal = timestamp

    def __str__(self) -> str:
        return self.__dict__.__str__()


class TradeFilter:
    """
        Class to filter queries to trades api
    """

    def __init__(self):
        self.sort = None
        self.by = None
        self._from = None
        self.till = None
        self.limit = None
        self.offset = None

    def sort_by(self, sort: SortDirection):
        """
        :param sort: Sort option SortDirection.ASC or DESC
        :returns self to build
        """

        self.sort = sort
        return self

    def filter_by(self, by: FilterBy):
        """
        :param by: Defines filter type
            Accepted values: id, timestamp
            Default value: timestamp
        :returns self to build
        """

        self.by = by
        return self

    def start_from(self, _from):
        """
        :param _from: Interval initial value (optional parameter) If sorting
        by timestamp is used, then Datetime, otherwise Number of index value
        :returns self to build
        """

        self._from = _from
        return self

    def until(self, till):
        """
        :param till: Interval end value (optional parameter) If sorting by
        timestamp is used, then Datetime, otherwise Number of index value
        """

        self.till = till
        return self

    def limit_by(self, limit):
        """
        :param limit: Default value: 100, Max value: 1000
        """

        self.limit = limit
        return self

    def with_offset(self, offset):
        """
        :param offset: Default value: 0, Max value: 100000
        """

        self.offset = offset
        return self

    def filter(self):
        """
            :returns a dictionary of filter items set
        """
        filter = {}

        for key in self.__dict__.keys():
            if self.__dict__[key]:
                if key == '_from':
                    filter['from'] = self.__dict__[key]
                    continue

                filter[key] = self.__dict__[key]

        return filter
