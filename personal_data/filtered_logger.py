#!/usr/bin/env python3

""" filter_datum function """

import re


def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str
    pattern = '|'.join(f'{field}{separator}.*?' for field in fields)
    return re.sub(pattern, lambda m: f'{m.group(0).split(separator)[0]}{separator}{redaction}', message)