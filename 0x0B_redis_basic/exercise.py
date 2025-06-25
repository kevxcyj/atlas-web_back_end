#!/usr/bin/env python3
 
import redis
import uuid
import functools
from typing import Union

def count_calls(method):
    """ Counts calls """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method):
    """ Stores inputs and outputs """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))
        return output
    return wrapper

def replay(method):
    """ Displays the history of calls """
    self = method.__self__
    qualname = method.__qualname__

    inputs_key = f"{qualname}:inputs"
    outputs_key = f"{qualname}:outputs"

    inputs = self._redis.lrange(inputs_key, 0, -1)
    outputs = self._redis.lrange(outputs_key, 0, -1)
   

    count = len(inputs)
    print(f"{qualname} was called {count} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{qualname}(*{inp.decode('utf-8')}) -> {out.decode('utf-8')}")

class Cache:
    """ Cache class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data and return key """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None):
        """ Retrieve value from Redis """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Returns value as string """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Returns value as integer """
        return self.get(key, fn=int)
