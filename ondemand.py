import sys

# default is to run locally
use_ondemand = "false"

# add the left/right decision
for arg in sys.argv:
    if arg.startswith("--ondemand"):
        parts = arg.split("=")
        use_ondemand = parts[1].lower()
        
if use_ondemand == "true":
    SELENIUM_HOST = "ondemand.saucelabs.com"
    SELENIUM_PORT = "4444"
    SAUCE_USERNAME = "your-sauce-user"
    SAUCE_KEY = "your-sauce-key-here"
    SAUCE_OS = "Windows 2003"
    SAUCE_BROWSER = "firefox"
    SAUCE_VERSION = "3."
    SAUCE_NAME = "Robots everywhere!"
    BROWSER = '{"username": "%s", "access-key": "%s", "os": "%s", "browser": "%s", "browser-version": "%s", "name": "%s"}' % (SAUCE_USERNAME, SAUCE_KEY, SAUCE_OS, SAUCE_BROWSER, SAUCE_VERSION, SAUCE_NAME)
else:
    SELENIUM_HOST = "localhost"
    SELENIUM_PORT = 4444
    BROWSER = "*firefox"

