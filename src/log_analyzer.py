#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
from argparse import ArgumentParser

# log_format ui_short '$remote_addr  $remote_user $http_x_real_ip [$time_local] "$request" '
#                     '$status $body_bytes_sent "$http_referer" '
#                     '"$http_user_agent" "$http_x_forwarded_for" "$http_X_REQUEST_ID" "$http_X_RB_USER" '
#                     '$request_time';

config = {
    "REPORT_SIZE": 1000,
    "REPORT_DIR": "./reports",
    "LOG_DIR": "./log",
    "LOGGING_PATH": "./logs/analyzer.log"
}

DEFAULT_CONFIG_PATH = './src/config.json'


def get_latest_log_path(log_dir: str) -> str:
    """Возвращает путь к файлу лога с последней датой"""
    pass


def main():
    latest_log_path = get_latest_log_path(config['LOG_DIR'])
    # read logs
    # analyze logs
    # calculate fields
    # render page
    # write page
    pass

def parse_config_path() -> str:
    parser = ArgumentParser()
    parser.add_argument(
        "--config", help="display a square of a given number",
        default=DEFAULT_CONFIG_PATH,
        type=str,
    )
    args = parser.parse_args()
    return args.config


def update_config_from_file(config_path: str):
    """Обновляет конфиг из файла"""

    with open(config_path, 'r') as config_file:
        if config_file.read() == '':
            logging.info(f"File {config_path} is empty. None of config arguments are updated.")
            return
        config_file.seek(0)
        try:
            new_config = json.load(config_file)
        except FileNotFoundError:
            raise ValueError(f"File {config_path} doesn\'t exist.")
        except json.decoder.JSONDecodeError:
            raise ValueError(f"File {config_path} must be JSON loadable.")

    config.update(new_config)
    logging.info(f"Config updated fron file {config_path}.")


if __name__ == "__main__":
    config_path = parse_config_path()
    update_config_from_file(config_path)

    logging.basicConfig(
        filename=config['LOGGING_PATH'],
        format='[%(asctime)s] %(levelname).1s %(message)s)',
        datefmt='%Y.%m.%d %H:%M:%S'
    )

    main()
