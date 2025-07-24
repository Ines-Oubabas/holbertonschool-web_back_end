#!/usr/bin/env python3
"""Filtered logger"""

import re
from typing import List
from typing import Tuple
import logging
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """filter obfuscate data in a log message"""
    for field in fields:
        message = re.sub(field + r"=[^" + separator + r"]*",
                         field + "=" + redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the formatter with fields to redact"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format log messages, redacting sensitive information"""
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """return logging.Logger"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)

    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """connect to the database using environnement variables"""
    db_connection = mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )
    return db_connection


def main():
    """Retrieve user data from the database and log it"""
    logger = get_logger()
    db = get_db()

    cursor = db.cursor()

    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]

    for row in cursor:
        str_row = "; ".join(f"{f}={r}" for r, f in zip(row, fields))
        log.info(str_row)

    cursor.close()
    db.close()
