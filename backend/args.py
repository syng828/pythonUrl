import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--database_file",
        help="Database file name",
        required=True,
        type=str)
    parser.add_argument(
        "--host",
        help="Host for the server",
        default="0.0.0.0",
        type=str)
    parser.add_argument(
        "--port",
        help="Port for the server",
        default=8000,
        type=int)
    parser.add_argument(
        "--disable_random_alias",
        action="store_true",
        help="Disables random alias",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="count",
        default=0,
        help="Increase verbosity level"
    )
    return parser.parse_args()
