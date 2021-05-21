# platform-bl

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](http://docs.platformio.org/page/projectconf.html) file:

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
