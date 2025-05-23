#!/usr/bin/env python3

""" filter_datum function """

import re
import logging


def filter_datum(
    fields: list[str],
    redaction: str, 
    message: str,
    separator: str
) -> str:
    """ Returns log message obfuscated
    
    Args:
        fields <typing.List[str]>: List of fields
        redaction <class str>: Obfuscating fields
        message <class str>: Log line
        separator <class str>: Separating all fields

    Returns:
        Log message with obfuscated string
    """
    pattern = '|'.join(f'{field}{separator}.*?' for field in fields)
    result = re.sub(pattern, lambda m: f'{m.group(0).split(separator)[0]}{separator}{redaction}', message)
    return f"{result}"


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError

