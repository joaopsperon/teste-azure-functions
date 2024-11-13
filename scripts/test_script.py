import logging
from os import getenv

ENVIROMENT_VARIABLE = getenv("ENVIROMENT_VARIABLE_1")


def main():
    logging.info(f"A variavel .env é: {ENVIROMENT_VARIABLE}")
