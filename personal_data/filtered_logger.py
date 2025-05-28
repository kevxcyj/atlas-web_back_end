#!/usr/bin/env python3
""" filter_datum module  """

import re
from typing import List
import logging


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
