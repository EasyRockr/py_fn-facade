import logging
from logging import Logger as PythonLogger
class Logger():

    def __init__(self):
        self.__logger:PythonLogger = logging.getLogger("MyApp")
        formatter = '%(asctime)s - [%(levelname)s] - (%(filename)s:%(lineno)d - %(funcName)s) - %(message)s'
        logging.basicConfig(filename="my_app.log", level=logging.DEBUG, format=formatter)

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Logger, cls).__new__(cls)
            print("new instance")
        return cls.instance
    

    def get_logger(self) -> PythonLogger:
        return self.__logger
    

    # telemetry logging

    # __counter = 0
    # def set_counter(self, value):
    #     self.__counter = value

    # def test(self):
    #     print(f"test {self.__counter}")
    