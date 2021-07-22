import logging
import time
from env import ENDPOINT, ACCESS_ID, ACCESS_KEY, USERNAME, PASSWORD
from tuya_iot import (
    TuyaOpenAPI,
    ProjectType,
    TuyaOpenMQ,
    TuyaDeviceManager,
    TuyaHomeManager,
    TuyaDeviceListener,
    TuyaDevice,
    TuyaTokenInfo,
    tuya_logger
)

tuya_logger.setLevel(logging.DEBUG)
# Init
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY, ProjectType.INDUSTY_SOLUTIONS)

openapi.login(USERNAME, PASSWORD)
openmq = TuyaOpenMQ(openapi)
openmq.start()

deviceManager = TuyaDeviceManager(openapi, openmq)


device = deviceManager.deviceMap.get(DEVICE_ID)


time.sleep(1000)
deviceManager.sendCommands(device.id, [{'code': 'switch_1', 'value': True}])

print('status: ', device.status)


