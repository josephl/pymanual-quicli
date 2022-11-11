# TODO: A script created with quick-python

import argparse
from configparser import ConfigParser
import logging
import signal
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
    parser.add_argument(
        "-b",
        "--break-int",
        action="store_true",
        help="Capture SIGINT with breakpoint (Keyboard Interrupt/Ctrl+C)",
    )
    args = parser.parse_args()
    config = ConfigParser()
    if args.config:
        config.read(args.config)
    logging_args = (
        config["logging"]
        if "logging" in config
        else {
            "format": "%(asctime)s %(levelname)s %(filename)s:%(funcName)s:%(lineno)d - %(message)s",
        }
    )
    set_logging(vcount=args.verbose, **logging_args)
    return args, config


def sigint_handler(sig, frame):
    logging.exception(f"Handled signal {sig} at: {frame}")
    breakpoint()


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
    try:
        main()
    except Exception:
        raise
    finally:
        duration = time() - start
        logging.info(f"Completed running '{__file__}' in {duration:0.03f} seconds")
