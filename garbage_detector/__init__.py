import logging
from os import path

from dotted.collection import DottedDict
from piny import YamlLoader

LOG_FORMAT = '%(asctime)s.%(msecs)03d [%(levelname)s] %(module)s.%(funcName)s:%(lineno)d (%(process)d:' \
    '%(threadName)s) - %(message)s'

LOG_LEVEL = 'INFO'

logging.basicConfig(format=LOG_FORMAT)
logging.getLogger().setLevel(LOG_LEVEL)

# @todo parametrize this
config = DottedDict(
    YamlLoader(
        path='/home/pi/Documents/Projects/garbage-detector-app/configs/app/default.yml',
    ).load(),
)

BASE_PATH = path.dirname(__file__) + '/..'
