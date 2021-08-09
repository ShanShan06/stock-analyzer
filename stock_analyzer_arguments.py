import argparse
from pathlib import Path


class StockAnalyzerArguments:
    def __init__(self, args=None):
        parser = self.create_parser()
        self.args = parser.parse_args(args)

    @staticmethod
    def create_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--input_file', help='path to the input file')
        parser.add_argument('-o', '--output_file', help='path to the output file')
        return parser

    @property
    def input_file(self):
        return self.args.input_file

    @property
    def output_file(self):
        # create parent directory if not exist
        path = Path(self.args.output_file)
        parent_dir = path.parent.absolute()
        Path(parent_dir).mkdir(parents=True, exist_ok=True)

        return self.args.output_file

