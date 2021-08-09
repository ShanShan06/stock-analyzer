from trade import Trade


class TradeAggregator:
    """
    TradeAggregator represent an aggregator of the trade statistics for a
    specific symbol.

    The aggregator is used to accepts a Trade instance, and accumulate or
    aggregate the statistics. Once all trades are aggregated, produce an
    output, by calling output() to present the required output statistics.
    """

    def __init__(self):
        self.total_volume = 0
        self.total_value = 0
        self.max_price = 0
        self.max_time_gap = 0
        self.last_ts = 0
        self.symbol = ''

    def _validate(self, trade):
        if len(self.symbol) != 0 and trade.symbol != self.symbol:
            raise ValueError(f'Invalid symbol: Received={trade.symbol}, Expected={self.symbol}')

    def accept(self, trade: Trade):
        """Accepts a trade transaction and accumulate its result.
        """
        self._validate(trade)
        self.symbol = trade.symbol
        self.total_volume += trade.quantity
        self.total_value += (trade.quantity * trade.price)
        self.max_price = max(self.max_price, trade.price)

        # calculate the timestamp gap from the last trade
        gap = self.last_ts > 0 and trade.timestamp - self.last_ts or 0
        self.max_time_gap = max(gap, self.max_time_gap)

        # done the accumulation, last_ts is no the current trade's timestamp
        self.last_ts = trade.timestamp

    def output(self):
        """Return the aggregation result values as tuple.

        As per requirements, the result value is a tuple as below:
        (<symbol>,<MaxTimeGap>,<Volume>,<WeightedAveragePrice>,<MaxPrice>)
        """
        # calculate volumn weighted average price, consider divided by 0
        vwap = self.total_volume and int(self.total_value / self.total_volume) or 0

        return (
            self.symbol,
            self.max_time_gap,
            self.total_volume,
            # volumn weighted average price truncated to integer
            vwap,
            self.max_price
        )

    def formatted_output(self):
        """Util method to format output as required.
        """
        return ','.join(map(str, self.output()))
    
