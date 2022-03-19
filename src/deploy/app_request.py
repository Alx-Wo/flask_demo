import argparse

import requests


def parse_arguments():
    """Parse cmd line arguments
    """
    parser = argparse.ArgumentParser(description="Command line parser for request arguments")
    parser.add_argument("input_text", help="Text to run a prediction on", type=str)
    return parser.parse_args()


def main():
    """main method
    """
    args = parse_arguments()
    server = "http://localhost:5000/prediction_api"

    response = requests.post(server, json={"input": args.input_text})
    print(response.json())


if __name__ == "__main__":
    main()
