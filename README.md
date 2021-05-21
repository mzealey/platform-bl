# platform-bl

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](http://docs.platformio.org/page/projectconf.html) file:

TODO:
- A better approach is probably to do as in package_bouffalo_index.json and just pull the precompiled files down, because I can't figure out how to get the bl_iot_sdk library building the libs

## Stable version

```ini
[env:stable]
platform = bl
board = bl602
framework = arduino
platform_packages = framework-arduinobouffalo @ https://github.com/mzealey/ArduinoCore-bouffalo.git
        framework-bl-iot-sdk @ https://github.com/mzealey/bl_iot_sdk.git
...
```

## Development version

```ini
[env:development]
platform = https://github.com/mzealey/platform-bl.git
board = ...
...
```

# Configuration

Please navigate to [documentation](http://docs.platformio.org/page/platforms/gd32v.html).
