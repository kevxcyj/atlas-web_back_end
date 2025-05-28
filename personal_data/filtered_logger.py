#!/usr/bin/env python3
""" filter_datum module  """

import re

def filter_datum(fields, redaction, message, separator):
    """ Filter_datum function """
    pattern = '|'.join(f'{field}{separator}.*?' for field in fields)
    return re.sub(pattern, lambda m: f'{m.group(0).split(separator)[0]}{separator}{redaction}', message)
