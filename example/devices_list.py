import logging
from tuya_iot import TuyaOpenAPI, tuya_logger

from env import *

tuya_logger.setLevel(logging.DEBUG)
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.login(USERNAME, PASSWORD)


openapi.get('/v1.0/iot-02/assets/{}/devices'.format(ASSET_ID))

