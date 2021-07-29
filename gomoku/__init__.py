import logging.config
import os

import yaml

path = os.path.dirname(os.path.realpath(__file__))
logconfig = os.path.join(path, '../logging.yaml')
with open(logconfig, 'r') as stream:
    config = yaml.load(stream, Loader=yaml.FullLoader)
logging.config.dictConfig(config)


X = 'X'
O = 'O'
EMPTY = ' '
SIZE = 10
