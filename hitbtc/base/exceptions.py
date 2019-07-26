class TradeException(Exception):
    """
        :param status_code the status code of response
        :param code the error code associated
        :param message human readable error message
        :param description any additional description field
    """

    def __init__(self, status_code: int, code: int, message: str, description:
    str):
        self.status_code = status_code
        self.code = code
        self.message = message
        self.description = description

    def __str__(self) -> str:
        return self.__dict__.__str__()
