from os.path import isdir, join

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()

board = env.BoardConfig()

FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-arduinobouffalo")
assert FRAMEWORK_DIR and isdir(FRAMEWORK_DIR)
SDK_DIR = env.PioPlatform().get_package_dir("framework-bl-iot-sdk")
assert SDK_DIR and isdir(SDK_DIR)

env.SConscript("_bare.py", exports="env")

env.Append(
    CPPDEFINES=[
        ("ARDUINO", 10805),
        ("ARDUINO_VARIANT", '\\"%s\\"' % env.BoardConfig().get("build.variant").replace('"', "")),
        ("ARDUINO_BOARD", '\\"%s\\"' % env.BoardConfig().get("build.board_def").replace('"', ""))
    ],

    CPPPATH=[
        join(FRAMEWORK_DIR, "cores", "bl602"),
        join(SDK_DIR, "components", "bl602/freertos_riscv/config"),
        join(SDK_DIR, "components", "bl602/freertos_riscv/portable/GCC/RISC-V"),
        join(SDK_DIR, "components", "bl602/bl602"),
        join(SDK_DIR, "components", "bl602/bl602/include"),
        join(SDK_DIR, "components", "bl602/bl602_std"),
        join(SDK_DIR, "components", "bl602/bl602_std/include"),
        join(SDK_DIR, "components", "bl602/bl602_std/bl602_std/StdDriver/Inc"),
        join(SDK_DIR, "components", "bl602/bl602_std/bl602_std/Device/Bouffalo/BL602/Peripherals"),
        join(SDK_DIR, "components", "bl602/bl602_std/bl602_std/RISCV/Device/Bouffalo/BL602/Startup"),
        join(SDK_DIR, "components", "bl602/bl602_std/bl602_std/RISCV/Core/Include"),
        join(SDK_DIR, "components", "bl602/bl602_std/bl602_std/Include"),
        join(SDK_DIR, "components", "bl602/bl602_std/bl602_std/Common/platform_print"),
        join(SDK_DIR, "components", "bl602/bl602_std/bl602_std/Common/soft_crc"),
        join(SDK_DIR, "components", "bl602/bl602_std/bl602_std/Common/partition"),
        join(SDK_DIR, "components", "bl602/bl602_std/bl602_std/Common/xz"),
        join(SDK_DIR, "components", "bl602/bl602_std/bl602_std/Common/cipher_suite/inc"),
        join(SDK_DIR, "components", "bl602/bl602_std/bl602_std/Common/ring_buffer"),
        join(SDK_DIR, "components", "stage/blfdt"),
        join(SDK_DIR, "components", "stage/blfdt/include"),
        join(SDK_DIR, "components", "stage/blfdt/inc"),
        join(SDK_DIR, "components", "sys/blmtd"),
        join(SDK_DIR, "components", "sys/blmtd/include"),
        join(SDK_DIR, "components", "sys/blmtd/include"),
        join(SDK_DIR, "components", "stage/blog"),
        join(SDK_DIR, "components", "stage/blog/include"),
        join(SDK_DIR, "components", "stage/blog"),
        join(SDK_DIR, "components", "stage/blog_testc"),
        join(SDK_DIR, "components", "stage/blog_testc/include"),
        join(SDK_DIR, "components", "stage/blog_testc"),
        join(SDK_DIR, "components", "sys/bloop/bloop"),
        join(SDK_DIR, "components", "sys/bloop/bloop/include"),
        join(SDK_DIR, "components", "sys/bloop/bloop/include"),
        join(SDK_DIR, "components", "sys/bltime"),
        join(SDK_DIR, "components", "sys/bltime/include"),
        join(SDK_DIR, "components", "sys/bltime/include"),
        join(SDK_DIR, "components", "stage/cli"),
        join(SDK_DIR, "components", "stage/cli/include"),
        join(SDK_DIR, "components", "stage/cli/cli/include"),
        join(SDK_DIR, "components", "bl602/freertos_riscv_ram"),
        join(SDK_DIR, "components", "bl602/freertos_riscv_ram/include"),
        join(SDK_DIR, "components", "bl602/freertos_riscv_ram/config"),
        join(SDK_DIR, "components", "bl602/freertos_riscv_ram/portable/GCC/RISC-V"),
        join(SDK_DIR, "components", "bl602/freertos_riscv_ram/portable/GCC/RISC-V/chip_specific_extensions/RV32F_float_abi_single"),
        join(SDK_DIR, "components", "bl602/freertos_riscv_ram/panic"),
        join(SDK_DIR, "components", "hal_drv"),
        join(SDK_DIR, "components", "hal_drv/include"),
        join(SDK_DIR, "components", "hal_drv/bl602_hal"),
        join(SDK_DIR, "components", "sys/bloop/looprt"),
        join(SDK_DIR, "components", "sys/bloop/looprt/include"),
        join(SDK_DIR, "components", "sys/bloop/loopset"),
        join(SDK_DIR, "components", "sys/bloop/loopset/include"),
        join(SDK_DIR, "components", "fs/romfs"),
        join(SDK_DIR, "components", "fs/romfs/include"),
        join(SDK_DIR, "components", "utils"),
        join(SDK_DIR, "components", "utils/include"),
        join(SDK_DIR, "components", "fs/vfs"),
        join(SDK_DIR, "components", "fs/vfs/include"),
        join(SDK_DIR, "components", "fs/vfs/posix/include"),
        join(SDK_DIR, "components", "stage/yloop"),
        join(SDK_DIR, "components", "stage/yloop/include"),
    ],

    LIBPATH=[
        join(SDK_DIR, "toolchain/riscv/Linux/riscv64-unknown-elf/", "lib"),
        join(SDK_DIR, "toolchain/riscv/Linux/riscv64-unknown-elf/", "ld"),
    ],

    LIBS=[
        #"c"
        "bl602",
        "bl602_std",
        "blfdt",
        "blmtd",
        "blog",
        "blog_testc",
        "bloop",
        "bltime",
        "cli",
        "freertos_riscv_ram",
        "hal_drv",
        "looprt",
        "loopset",
        "romfs",
        "utils",
        "vfs",
        "yloop",
    ],

    LIBSOURCE_DIRS=[
        join(FRAMEWORK_DIR, "libraries")
    ],
)

#if not env.BoardConfig().get("build.ldscript", ""):
#    env.Replace(LDSCRIPT_PATH=join(
#        SDK_DIR, "RISCV", "env_Eclipse", board.get("build.arduino.ldscript")))

#
# Target: Build Core Library
#

libs = []

#if "build.variant" in env.BoardConfig():
#    env.Append(
#        CPPPATH=[
#            join(FRAMEWORK_DIR, "variants",
#                 env.BoardConfig().get("build.variant"))
#        ]
#    )
#    libs.append(env.BuildLibrary(
#        join("$BUILD_DIR", "FrameworkArduinoVariant"),
#        join(FRAMEWORK_DIR, "variants", env.BoardConfig().get("build.variant"))
#    ))

envsafe = env.Clone()

# TODO: run 'make' in the SDK directory to build it
#libs.append(envsafe.BuildLibrary(
#    join("$BUILD_DIR", "FrameworkArduino"),
#    join(FRAMEWORK_DIR, "cores", "arduino")
#))

env.Prepend(LIBS=libs)
