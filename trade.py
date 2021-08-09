from dataclasses import dataclass


@dataclass
class Trade:
    """Trade represents the input trade transaction
    """
    timestamp: int
    symbol: str
    quantity: int
    price: int

    @classmethod
    def parse(cls, line: str):
        """make a proper Trade object out of line of string.
        """
        timestamp, symbol, quantity, price = line.strip().split(',')
        return cls(int(timestamp), symbol, int(quantity), int(price))

