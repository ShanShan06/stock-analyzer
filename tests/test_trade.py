from trade import Trade


def test_parse():
    line = "51300000871,adg,24,285\n"
    trade = Trade.parse(line)
    assert trade.timestamp == 51300000871
    assert trade.symbol == "adg"
    assert trade.quantity == 24
    assert trade.price == 285

