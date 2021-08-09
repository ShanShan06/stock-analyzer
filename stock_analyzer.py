import logging

from stock_analyzer_arguments import StockAnalyzerArguments
from trade import Trade
from trade_aggregator import TradeAggregator


# set up basic logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filename='application.log')


def run(input_file, output_file):
    stock_statistics = {}

    for line in input_file:
        stripped_line = line.strip()
        if stripped_line:
            trade = Trade.parse(stripped_line)
            aggr = stock_statistics.setdefault(trade.symbol, TradeAggregator())
            if trade.symbol in stock_statistics:
                aggr.accept(trade)

    for key, value in sorted(stock_statistics.items()):
        output_file.write(value.formatted_output() + '\n')


if __name__ == "__main__":
    arguments = StockAnalyzerArguments()
    with open(arguments.input_file) as in_file, open(arguments.output_file, 'w') as out_file:
        run(in_file, out_file)
