import logging
from logging import Logger #type-hints
from util.logger import Logger as CustomLogger

logger:Logger = logging.getLogger("MyApp")

formatter = '%(asctime)s - [%(levelname)s] - (%(filename)s:%(lineno)d - %(funcName)s) - %(message)s'

logging.basicConfig(filename="my_app.log", level=logging.DEBUG, format=formatter)


def test_logs():
    logger.info("This is an info")
    logger.warning("This is a warning")
    logger.debug("This is a debug")
    logger.error("This is an error")

# test_logs()


logger1 = CustomLogger()
logger2 = CustomLogger()
logger3 = CustomLogger()


logger1.set_counter(99)
logger1.test()
logger2.test()
logger3.test()
print("logging completed")

# singleton = one object only