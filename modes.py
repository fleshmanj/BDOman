from abc import ABC, abstractmethod
import inspect
import logging


class AbstractMode(ABC):

    def __init__(self, d):
        logging.debug("created")

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def use_keyboard_input(self, kb: dict):
        pass

    @abstractmethod
    def screen(self):
        pass


class FishingMode(AbstractMode):

    def __int__(self):
        logging.debug("Created fishing mode")
