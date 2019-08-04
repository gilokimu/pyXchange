# PyExchange
Scope of the project has change - Python wrapper for several cryptocurrency exchange APIs.

# Currently supports
1. Hitbtc

## Previously
Rest client implementation of the HITBTC API according to the rest doc <a href="https://api.hitbtc.com/">here</a>

# Motivation
Most crypto API on github only either provide a guide on how to retrieve data or provide a json dump which quickly becomes unmaintainably as the complexity of the project kicks in. This project seeks to structure data responses from hitbtc API and eventually become augnestic of the crypto exchange  

# !!! Under Construction !!!
I am still moving files around, once done, I will provide documentation on how to use the client. 

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
