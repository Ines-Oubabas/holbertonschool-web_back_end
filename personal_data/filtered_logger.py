#!/usr/bin/env python3
"""
This module implements a logging system with PII field redaction.
It includes functions to filter sensitive data, configure logging,
connect to a MySQL database, and log user information safely.
"""

import re
import logging
from typing import List
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Obfuscates specified fields in the given message string.

    Args:
        fields (List[str]): List of field names to obfuscate.
        redaction (str): The redaction string to replace field values with.
        message (str): The input log message.
        separator (str): The field separator.

    Returns:
        str: The obfuscated log message.
    """
    return re.sub(
        rf"({'|'.join(fields)})=([^{separator}]+)",
        lambda m: f"{m.group(1)}={redaction}",
        message
    )


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """
    Formatter class that redacts sensitive information from log records.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize formatter.

        Args:
            fields (List[str]): List of fields to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format log record and redact sensitive fields.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted and redacted log string.
        """
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION, original, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger named 'user_data'.

    Returns:
        logging.Logger: Configured logger.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Establishes a secure connection to the MySQL database using env variables.

    Returns:
        MySQLConnection: A MySQL database connection object.
    """
    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def main():
    """
    Main function that logs user data with sensitive fields redacted.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()

    for row in cursor:
        message = "; ".join(
            f"{desc[0]}={str(val)}" for val, desc in zip(row, cursor.description)
        )
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
