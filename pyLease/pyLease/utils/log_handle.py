# coding:utf-8
import os
import yaml
import logging
import logging.config

from ..settings import LOCAL_LOG_DIR


def init_logging(path="./logging.yaml", level=logging.INFO):
    """初始化logging"""
    if os.path.exists(path):
        with open(path, 'rt') as f:
            log_config = yaml.load(f.read())
            log_config["root"]["level"] = level
            log_config["handlers"]["info_file_handler"]["filename"] = os.path.join(LOCAL_LOG_DIR, "info.log")
            log_config["handlers"]["error_file_handler"]["filename"] = os.path.join(LOCAL_LOG_DIR, "error.log")
        logging.config.dictConfig(log_config)
    else:
        logging.basicConfig(level=level)
    # logger = logging.getLogger()
    # logger.info("初始化logging完成")
    # return logger
