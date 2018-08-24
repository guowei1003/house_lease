# coding:utf-8

import threading
from pyLease.pyLease.utils.database import Connection
from pyLease.pyLease.utils.log_handle import init_logging
from pyLease.pyLease.settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

con = None
mutex = threading.Lock()
logger = init_logging()


def connect():
    """
    get db connect
    :return:
    """
    global con, mutex
    if con and con._db:
        return con

    con = Connection(MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, time_zone="+8:00", mutex=mutex)
    logger.info("启动MySQL")
    return con


def _ping_db():
    """
    Judge whether the database is alive
    :return:
    """
    global con
    status = False
    if con:
        try:
            con.query("show variables")
            status = True
        except Exception as e:
            logger.error(e)
            status = False
    logger.info("DB is active: %s" % status)
    return status
