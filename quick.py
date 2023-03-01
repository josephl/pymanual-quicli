# TODO: A script created with quick-python

import argparse
from configparser import ConfigParser
import logging
from time import time
from typing import Any, Dict, Optional, Tuple


def parse_args() -> Tuple[argparse.Namespace, ConfigParser]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        action="append",
        help="Config path(s)",
    )
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Verbose logging"
    )
    args = parser.parse_args()
    config = ConfigParser()
    for config_path in args.config or []:
        config.read(config_path)
    logging_args = (
        config["logging"]
        if "logging" in config
        else {
            "format": "%(asctime)s %(levelname)s %(filename)s:%(funcName)s:%(lineno)d - %(message)s",
        }
    )
    set_logging(vcount=args.verbose, **logging_args)
    return args, config


def set_logging(vcount: Optional[int] = 0, **log_args: Dict[str, Any]) -> None:
    """
    Apply logging options to `logging.basicConfig`
    """
    if vcount >= 2:
        log_args["level"] = logging.DEBUG
    elif vcount == 1:
        log_args["level"] = logging.INFO
    logging.basicConfig(**log_args)


def main():
    args, config = parse_args()
    if args.break_int:
        signal.signal(signal.SIGINT, sigint_handler)
    pass


if __name__ == "__main__":
    start = time()
    caught_exc = None
    try:
        main()
    except Exception as exc:
        caught_exc = exc
        raise
    finally:
        duration = time() - start
        if caught_exc:
            logging.exception(caught_exc)
        prefix = "Failed" if caught_exc else "Completed"
        logging.info(f"{prefix} running '{__file__}' in {duration:0.03f} seconds")
