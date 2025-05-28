#!/usr/bin/env python3
""" Ecryption for passwords """

import bcrypt


def hash_password(password: str) -> bytes:
    """ hash_password function """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ is_valid function """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
