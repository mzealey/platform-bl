from SCons.Script import Import

Import("env")

board = env.BoardConfig()

sdk_version='release_bl_iot_sdk_1.6.11-1-g66bb28da-dirty'
phy_ver='a0_final-44-geb7fadd'
rf_ver='f76e39a'

env.Append(

    ASFLAGS = ["-x", "assembler-with-cpp"],

    CCFLAGS=[
        "-Os",
        "-Wall", 
        "-march=%s" % board.get("build.march"),
        "-mabi=%s" % board.get("build.mabi"),
        #"-mcmodel=%s" % board.get("build.mcmodel"),
        "-gdwarf",
        "-ffunction-sections",
        "-fdata-sections",
        "-fstrict-volatile-bitfields",
        "-fshort-enums",
        "-ffreestanding",
        "-fno-strict-aliasing",
        "-fno-use-cxa-atexit",
        "-nostdlib",
        "-Wpointer-arith",
        "-fexceptions",
        "-fstack-protector",
        "-fno-rtti",
        "-fno-exceptions",
        "-fms-extensions",
        "-Werror=return-type",
        "-MMD",
        "-DBL_SDK_VER=" + sdk_version,
        "-DBL_SDK_PHY_VER=" + phy_ver,
        "-DBL_SDK_RF_VER=" + rf_ver,
        "-DARDUINO_BOUFFALO",
        "-DBL602",
        "-DCONF_USER_ENABLE_PSRAM",
        "-DconfigUSE_TICKLESS_IDLE=0",
        "-DFEATURE_WIFI_DISABLE=1",
        "-DCFG_FREERTOS",
        "-DARCH_RISCV",
        "-DBL602",
        "-DCONFIG_SET_TX_PWR",
        "-DCFG_BLE_ENABLE",
        "-DBFLB_BLE",
        "-DCFG_BLE",
        "-DCFG_SLEEP",
        "-DOPTIMIZE_DATA_EVT_FLOW_FROM_CONTROLLER",
        "-DCFG_CON=2",
        "-DCFG_BLE_TX_BUFF_DATA=2",
        "-DCONFIG_BT_ALLROLES",
        "-DCONFIG_BT_CENTRAL",
        "-DCONFIG_BT_OBSERVER",
        "-DCONFIG_BT_PERIPHERAL",
        "-DCONFIG_BT_BROADCASTER",
        "-DCONFIG_BT_L2CAP_DYNAMIC_CHANNEL",
        "-DCONFIG_BT_GATT_CLIENT",
        "-DCONFIG_BT_CONN",
        "-DCONFIG_BT_GATT_DIS_PNP",
        "-DCONFIG_BT_GATT_DIS_SERIAL_NUMBER",
        "-DCONFIG_BT_GATT_DIS_FW_REV",
        "-DCONFIG_BT_GATT_DIS_HW_REV",
        "-DCONFIG_BT_GATT_DIS_SW_REV",
        "-DCONFIG_BT_ECC",
        "-DCONFIG_BT_GATT_DYNAMIC_DB",
        "-DCONFIG_BT_GATT_SERVICE_CHANGED",
        "-DCONFIG_BT_KEYS_OVERWRITE_OLDEST",
        "-DCONFIG_BT_KEYS_SAVE_AGING_COUNTER_ON_P",
        "-DCONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS",
        "-DCONFIG_BT_BONDABLE",
        "-DCONFIG_BT_HCI_VS_EVT_USER",
        "-DCONFIG_BT_ASSERT",
        "-DCONFIG_BT_SMP",
        "-DCONFIG_BT_SIGNING",
        "-DCONFIG_BT_SETTINGS_CCC_LAZY_LOADING",
        "-DCONFIG_BT_SETTINGS_USE_PRINTK",
        "-DCFG_BLE_STACK_DBG_PRINT",
        "-DBL_CHIP_NAME=BL602",
        "-DARCH_RISCV",
        "-DCONFIG_PSM_EASYFLASH_SIZE=16384",
        "-DconfigUSE_TICKLESS_IDLE=0",
        "-DFEATURE_WIFI_DISABLE=1",
        "-DCFG_BLE_ENABLE",
        "-DCONF_USER_ENABLE_PSRAM",
        "-DCONF_USER_ENABLE_VFS_ROMFS",
        "-DCFG_COMPONENT_BLOG_ENABLE=0",
    ],

    CFLAGS = [
        "-std=gnu11"
    ],

    CXXFLAGS = [
        "-std=gnu++11"
    ],

    CPPDEFINES = [
        "USE_STDPERIPH_DRIVER",
        #("HXTAL_VALUE", "%sU" % board.get("build.hxtal_value"))
    ],

    LINKFLAGS=[
        "-march=%s" % board.get("build.march"),
        "-mabi=%s" % board.get("build.mabi"),
        #"-mcmodel=%s" % board.get("build.mcmodel"),
        "-nostartfiles",
        "-Xlinker",
        "--gc-sections",
        #"--specs=nano.specs"
        # "-Wl,--wrap=_exit",
        # "-Wl,--wrap=close",
        # "-Wl,--wrap=fatat",
        # "-Wl,--wrap=isatty",
        # "-Wl,--wrap=lseek",
        # "-Wl,--wrap=read",
        # "-Wl,--wrap=sbrk",
        # "-Wl,--wrap=stub",
        # "-Wl,--wrap=write_hex",
        # "-Wl,--wrap=write"
    ],

    #LIBS=["c"]
)


# copy CCFLAGS to ASFLAGS (-x assembler-with-cpp mode)
env.Append(ASFLAGS=env.get("CCFLAGS", [])[:])
