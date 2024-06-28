# pyElexon
Python package wrapper around Elexon api

In Progress

It would be great to create a python package that wraps around the new Elexon API - https://developer.data.elexon.co.uk/

See issues for things to do

Motivated by https://github.com/OSUKED/ElexonDataPortal

## Examples

To get the balancing system prices on 2024-04-01
```python
from pyelexon.balancing.settlement.main import get_system_prices
df = get_system_prices("2024-04-01")
prices = df["systemSellPrice"]
```