# 8A1.3) Wish for Wings

Define the dataclass `Bird` with the fields `name` (str), `can_fly` (bool), and `region` (str). Some example birds are provided below.

Then, define the function `first_land_bird` that consumes a list of `Bird` and produces the `name` of the first `Bird` in the list that cannot fly. If there are no birds that cannot fly, then return `"Flew the coop"` instead.


```python
from dataclasses import dataclass
from bakery import assert_equal



boids = [
    Bird("Zazu", True, "Africa"),
    Bird("Iago", True, "Agrabah"),
    Bird("Opus", False, "Antarctica"),
    Bird("Huey", False, "Duckberg"),
    Bird("Bess", True, "Ga'Hoole")
]
```