# tuya-smart-plug

This project is developed using Tuya SDK, which enables you to quickly develop smart devices, branded APP, cloud development project, etc.

For more information, please check Tuya Developer Click and Connect Challenge https://pages.tuya.com/develop/ClickAndConnect_TuyaDeveloper?_source=e9684c7ca6b31e7221c8420f5af94631

## Requirements

```
pip3 install tuya-iot-py-sdk
```


## Device control
- TuyaDeviceManager
	- get_device_info
	- get_device_list_info
	- remove_device
	- remove_device_list
	- get_factory_info
	- factory_reset
	- get_device_status
	- get_device_list_status
	- get_device_functions
	- get_category_functions
	- get_device_specification
	- send_commands
<br>

## Sample code

```
import logging
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
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY, ProjectType.INDUSTY_SOLUTIONS)

openapi.login(USERNAME, PASSWORD)
openmq = TuyaOpenMQ(openapi)
openmq.start()

deviceManager = TuyaDeviceManager(openapi, openmq)


device = deviceManager.deviceMap.get(DEVICE_ID)



deviceManager.sendCommands(device.id, [{'code': 'switch_1', 'value': True}])

print('status: ', device.status)

```

## Docx:

![PyPI](https://img.shields.io/pypi/v/tuya-iot-py-sdk)

![PyPI - Downloads](https://img.shields.io/pypi/dm/tuya-iot-py-sdk)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tuya-iot-py-sdk)


<br>


## Registration

Please check [Tuya IoT Platform Configuration Guide](https://developer.tuya.com/en/docs/iot/Configuration_Guide_custom?id=Kamcfx6g5uyot) to register an account on the [Tuya IoT Platform](https://iot.tuya.com?_source=github), and get the required information. <br>
You need to create a Cloud project and complete the configuration of asset, user, and application. Then, you will get the **username**, **password**, **Access ID**, and **Access Secret**.


