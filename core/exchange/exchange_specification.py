from abc import ABC


class ExchangeSpecification(ABC):
    exchange_name: str
    exchange_description: str
    username: str
    password: str
    secret_key: str
    api_key: str
    ssl_url: str
    plain_text_url: str
    host: str
