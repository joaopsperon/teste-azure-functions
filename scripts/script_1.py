import logging
from os import getenv


def main():
    ENVIROMENT_VARIABLE = getenv("ENVIROMENT_VARIABLE_1")
    logging.info(f"A variavel .env é: {ENVIROMENT_VARIABLE}")
