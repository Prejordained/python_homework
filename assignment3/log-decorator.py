# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {list(args) if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"return: {result}")
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello World!")

@logger_decorator
def takes_positional(*args):
    return True

@logger_decorator
def takes_keyword(**kwargs):
    return logger_decorator

say_hello()
takes_positional(1, 2, 3)
takes_keyword(name="Jordan", age=35)
