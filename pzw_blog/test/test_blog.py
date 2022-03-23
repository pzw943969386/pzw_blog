from typing import Any, Callable, Union
from logging import logger

def retry(retry_time: int = 3) -> Callable:
    def decorator(function: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            count = 0
            while count < retry_time:
                try:
                    return function(*args, **kwargs)
                except Exception as e:
                    logger.exception(e)
                    count += 1
            return function(*args, *kwargs)

        return wrapper

    return decorator
