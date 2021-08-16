# TODO: A script created with quick-python

import argparse
from configparser import ConfigParser
import logging
import typing


DEFAULT_CFG_PATH = "config.ini"


def parse_args() -> typing.Tuple[argparse.Namespace, ConfigParser]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config", action="append", help="Config path(s)",
    )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Verbose logging"
    )
    args = parser.parse_args()
    config = ConfigParser()
    config.read(args.config)
    logging_args = config["logging"]
    set_logging(vcount=args.verbose, **logging_args)
    return args, config


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
    args, config = parse_args()
