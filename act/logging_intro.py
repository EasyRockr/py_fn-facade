from util.logger import Logger

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"begin additional behavior [{args}] -- [{kwargs}]")
        result = func(*args, **kwargs)
        print("end: additional behavior")
        return result
    return wrapper

# @my_decorator
def add(*args):
    print("begin additional behavior")
    print(args)
    print("end: additional behavior")

@my_decorator
def test(**kwargs):
    print(kwargs)

# def all(*args, **kwargs):
#     print(args)
#     print(kwargs)

add(1,2,3,4)
test(v1=2, v2=2)
# all(1,2,3,4, v1=1, v2=2)






















# positional muna bago keyword args
# function wrapper

# logger1 = Logger().get_logger()
# logger2 = Logger().get_logger()
# logger3 = Logger().get_logger()

# logger1.info("test1")
# logger2.info("test2")
# logger3.info("test3")
# print("logging completed")

# singleton = one object only









# import logging
# from logging import Logger #type-hints
# from util.logger import Logger as CustomLogger

# logger:Logger = logging.getLogger("MyApp")

# formatter = '%(asctime)s - [%(levelname)s] - (%(filename)s:%(lineno)d - %(funcName)s) - %(message)s'

# logging.basicConfig(filename="my_app.log", level=logging.DEBUG, format=formatter)


# def test_logs():
#     logger.info("This is an info")
#     logger.warning("This is a warning")
#     logger.debug("This is a debug")
#     logger.error("This is an error")

# # test_logs()


# logger1 = CustomLogger()
# logger2 = CustomLogger()
# logger3 = CustomLogger()


# logger1.set_counter(99)
# logger1.test()
# logger2.test()
# logger3.test()
# print("logging completed")

# # singleton = one object only