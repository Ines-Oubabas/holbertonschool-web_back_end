#!/usr/bin/env python3
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
    """Obfuscate the values of specified fields."""
    return re.sub(
        rf"({'|'.join(fields)})=([^{separator}]+)",
        lambda m: f"{m.group(1)}={redaction}",
        message
    )


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original = super().format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            original,
            self.SEPARATOR
        )


def get_logger() -> logging.Logger:
    """Returns a configured logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)

    return logger


def get_db() -> MySQLConnection:
    """Connect securely to a MySQL database using env variables."""
    return mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )


def main():
    """Main function that retrieves and logs data with obfuscated PII"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for row in cursor:
        message = "; ".join(
            f"{desc[0]}={str(val)}"
            for val, desc in zip(row, cursor.description)
        )
        logger.info(message)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
