import pytest

from trade import Trade
from trade_aggregator import TradeAggregator


def test_accept_one_trade():
    trade_aggregator = TradeAggregator()

    trade = Trade(51300000871, "adg", 24, 285)

    trade_aggregator.accept(trade)
    assert ("adg", 0, 24, 285, 285) == trade_aggregator.output()
    assert "adg,0,24,285,285" == trade_aggregator.formatted_output()


def test_accept_two_trades():
    trade_aggregator = TradeAggregator()

    trade1 = Trade(51300000871, "adg", 24, 285)
    trade2 = Trade(51300000872, "adg", 11, 111)

    trade_aggregator.accept(trade1)
    trade_aggregator.accept(trade2)

    assert ("adg", 1, 35, 230, 285) == trade_aggregator.output()
    assert "adg,1,35,230,285" == trade_aggregator.formatted_output()


def test_throw_exception_when_receiving_trade_for_unexpected_symbol():
    trade_aggregator = TradeAggregator()

    trade1 = Trade(51300000871, "abc", 24, 285)
    trade_aggregator.accept(trade1)

    trade2 = Trade(51300000872, "xyz", 11, 111)
    with pytest.raises(ValueError, match=r"Invalid symbol: Received=xyz, Expected=abc"):
        trade_aggregator.accept(trade2)


