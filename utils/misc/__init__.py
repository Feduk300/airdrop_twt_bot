import random

from . import logging



def gen_captcha():
    return random.randint(1000, 9999)
