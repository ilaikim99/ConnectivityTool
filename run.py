import argparse
import os
from connectivity_tester.test_handler import TestHandler


def main():
    default_input = os.path.join(os.path.dirname(__file__), "example/input.yaml")
    default_output = os.path.join(os.path.dirname(__file__), "example/results.csv")
    parser = argparse.ArgumentParser(description='Running Connectivity Tests')
    parser.add_argument('--input_file', type=str, default=default_input, help='yaml input file')
    parser.add_argument('--output_file', type=str, default=default_output, help='csv results output file')

    args = parser.parse_args()

    test_handler = TestHandler(args.input_file, args.output_file)
    test_handler.run_test()


if __name__ == "__main__":
    main()
