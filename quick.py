# TODO: A script created with quick-python

import argparse
from configparser import ConfigParser, SectionProxy
import logging
import typing


DEFAULT_CFG_PATH = "config.ini"
DEFAULT_CFG_SECTION = "CHANGEME"  # TODO: Edit this to a project section name


def parse_args() -> typing.Tuple[argparse.Namespace, SectionProxy]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config", default=DEFAULT_CFG_PATH, help="Config path",
    )
    parser.add_argument(
        "-s", "--config-section", default=DEFAULT_CFG_SECTION, help="Config section"
    )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Verbose logging"
    )
    args = parser.parse_args()
    cfg_parser = ConfigParser()
    cfg_parser.read(args.config)
    config = cfg_parser[args.config_section]
    logging_args = cfg_parser["logging"]
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
