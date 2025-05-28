#!/usr/bin/env python3
""" filter_datum module  """

import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates log message

    Args:
        fields: List of all fields
        redaction: String
        message: String for log line
        separator: Character separating fields

    Returns:
        Log message string with obfuscation
    """
    for field in fields:
        pattern: str = f"{field}=([^{separator}]*)"
        repl: str = f"{field}={redaction}"
        message = re.sub(pattern, repl, message)
    return message

def get_logger() -> logging.Logger:
    """ Get logger function """
    logger = logging.getLogger("user_data")
    
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()

    formatter = RedactingFormatter(PII_FIELDS)
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Set up mysql database """

    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "pw")
    host_name = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME", "my_db")

    connector_obj = mysql.connector.connect(
        user=user,
        password=password,
        host=host_name,
        database=db_name,
    )

    return connector_obj


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class

        Args:
            Logging.formatter: function
        Return:
            filter_datum
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Init function """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Format function """
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)
    
    def main():
        """Sets up logger through main function """
    logger: logging.Logger = get_logger()
    db: mysql.connector.connection.MySQLConnection = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    for row in cursor:
        preformatted_fields: list = []
        for key, value in row.items():
            preformatted_fields.append(f"{key}={value}")
        entry: str = "; ".join(preformatted_fields)
        logger.info(entry)
    cursor.close()
    db.close()


    if __name__ == "__main__":
        main()
