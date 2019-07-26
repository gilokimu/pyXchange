# Python HITBTC API
Rest client implementation of the HITBTC API according to the rest doc <a href="https://api.hitbtc.com/">here</a>

# !!! Under Construction !!!

##  Usage
To retrieve order you have made

```python
    api = OrderService()
    order = api.historical_orders()
    pprint(order)
```

And the output you will receive
```python
{
  'clientOrderId': '',
  'createdAt': datetime.datetime(2019, 7, 26, 3, 30, 25, 96000),
  'price': Decimal('9698.33'),
  'quantity': Decimal('0.00003'),
  'side': 'sell',
  'status': 'filled',
  'symbol': 'BTCUSD',
  'timeInForce': 'GTC',
  'type': 'limit',
  'updatedAt': datetime.datetime(2019, 7, 26, 3, 45, 0, 682000)
 }
```


## What's under the hood
### Implemented a declarative HTTP Client

