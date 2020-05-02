"""
quick.py

Template for most basic Python scripts
"""

import argparse
from configparser import ConfigParser
import logging
import typing


DEFAULT_CFG_PATH = "config.ini"
DEFAULT_CFG_SECTION = "DEFAULT"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config", nargs="?", default=DEFAULT_CFG_PATH, help="Config path",
    )
    parser.add_argument(
        "-s", "--config-section", default=DEFAULT_CFG_SECTION, help="Config section"
    )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Verbose logging"
    )

    args = parser.parse_args()
    set_logging(vcount=args.verbose)
    return args


def set_logging(vcount: typing.Optional[int] = None, **log_args: dict) -> None:
    """
    Apply logging options to `logging.basicConfig`
    """
    if vcount >= 2:
        log_args["level"] = logging.DEBUG
    elif vcount == 1:
        log_args["level"] = logging.INFO
    logging.basicConfig(**log_args)


if __name__ == "__main__":
    args = parse_args()
    cfg_parser = ConfigParser()
    cfg_parser.read(args.config)
    config = cfg_parser[args.config_section]
