import os
import subprocess

from dotenv import load_dotenv

load_dotenv()


def get_device_udid():
    adb_path = os.getenv("SDK_PLATFORM_TOOLS_PATH")
    adb_command = os.path.join(adb_path, "adb")
    result = subprocess.run([adb_command, "devices"], stdout=subprocess.PIPE, text=True)
    line = result.stdout.strip().split("\n")[1]
    udid = line.split()[0]
    return udid


def android_get_desired_capabilities():
    return {
        "autoGrantPermissions": True,
        "automationName": "uiautomator2",
        "newCommandTimeout": 500,
        "noSign": True,
        "platformName": "Android",
        "platformVersion": "10",
        "resetKeyboard": True,
        "systemPort": 8301,
        "takesScreenshot": True,
        "udid": get_device_udid(),
        "appPackage": "com.ajaxsystems",
        "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity"
    }
