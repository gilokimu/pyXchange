from requests import Response
from uplink import error_handler, response_handler

from hitbtc.base.exceptions import TradeException


@error_handler
def raise_api_error(exc_type, exc_val, exc_tb):
    """
    :param exc_type:  the type of the exception
    :param exc_val: the exception instance raised
    :param exc_tb: a traceback instance.
    """

    print(exc_type)
    print(exc_val)
    print(exc_tb)


@response_handler
def raise_for_status(response: Response):
    """
    A decorator for creating custom response handlers.
    :param response: a HTTP response object:
    :return:
    """

    if response.status_code != 200:
        error_body = response.json()['error']
        code = error_body['code']
        message = error_body['message']
        description = error_body['description']

        raise TradeException(status_code=response.status_code, code=code,
                             message=message,
                             description=description)

    return response
