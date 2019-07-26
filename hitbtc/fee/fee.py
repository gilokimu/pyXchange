import decimal


class Fee:
    take_liquidity_rate: decimal = None
    provide_liquidity_rate: decimal = None

    def __init__(self, take_liquidity_rate: decimal = None,
                 provide_liquidity_rate: decimal = None):
        self.take_liquidity_rate = take_liquidity_rate
        self.provide_liquidity_rate = provide_liquidity_rate
