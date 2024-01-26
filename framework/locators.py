from appium.webdriver.common.appiumby import AppiumBy

GO_TO_LOGIN_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/authHelloLogin")
EMAIL_FIELD = (AppiumBy.ID, "com.ajaxsystems:id/authLoginEmail")
PASSWORD_FIELD = (AppiumBy.ID, "com.ajaxsystems:id/authLoginPassword")
SUBMIT_LOGIN_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='Вхід']")
ADD_HUB_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/hubAdd")
SIDE_BAR_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/menuDrawer")
APP_SETTINGS = (AppiumBy.ID, "com.ajaxsystems:id/settings")
APP_HELP = (AppiumBy.ID, "com.ajaxsystems:id/help")
APP_LOGS = (AppiumBy.ID, "com.ajaxsystems:id/logs")
APP_CAMERA = (AppiumBy.ID, "com.ajaxsystems:id/camera")
APP_ADD_HUB = (AppiumBy.ID, "com.ajaxsystems:id/addHub")
APP_TERMS_OF_USE = (AppiumBy.ID, "com.ajaxsystems:id/documentation_text")
