import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as ff_Options
from selenium.webdriver.chrome.options import Options as chrome_Options
import os


def _browserstack_url():
    """Builds the BrowserStack remote URL from environment variables.
    Set BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY before running
    any Remote* browser fixture. Never hardcode these values."""
    username = os.environ["BROWSERSTACK_USERNAME"]
    access_key = os.environ["BROWSERSTACK_ACCESS_KEY"]
    return f"http://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub"


@pytest.fixture(params=["Chrome"], scope="session")
def init_driver(request):
    global driver
    """This checks chrome browser"""
    if request.param == "Chrome":
        options = chrome_Options()
        options.headless = False
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--use-fake-ui-for-media-stream")
        driver = webdriver.Chrome(options=options)

    """This checks Firefox browser"""
    if request.param == "Firefox":
        path = os.getcwd()
        options = ff_Options()
        options.headless = False
        driver = webdriver.Firefox(options=options, service_log_path=path + "/Logs/geckodriver.log")

    """This checks Safari browser"""
    if request.param == "Safari":
        driver = webdriver.Safari()

    if request.param == "RemoteIE":
        desired_cap = {
            'os': 'Windows',
            'os_version': '10',
            'browser': 'IE',
            'browser_version': '11.0',
            'resolution': '2048x1536',
            'name': "IETesting",
            'browserstack.local': 'true',
            'build': 'Test Build IE',
        }
        driver = webdriver.Remote(
            command_executor=_browserstack_url(),
            desired_capabilities=desired_cap
        )

    if request.param == "RemoteSafari":
        desired_cap = {
            'os': 'OS X',
            'os_version': 'Catalina',
            'resolution': '1920x1080',
            'browser': 'Safari',
            'browser_version': '13.1',
            'name': "SafariTesting",
            'browserstack.local': 'true',
            'build': 'BStack Build safari',
            'autoAcceptAlerts': 'true',
            'acceptSslCert': 'true'
        }
        driver = webdriver.Remote(
            command_executor=_browserstack_url(),
            desired_capabilities=desired_cap
        )

    if request.param == "RemoteChrome":
        desired_cap = {
            'os_version': 'Catalina',
            'resolution': '1920x1080',
            'browser': 'Chrome',
            'browser_version': 'latest',
            'os': 'OS X',
            'name': 'Chrome Testing',
            'build': 'Test Build Chrome',
            'browserstack.local': 'true',
        }
        driver = webdriver.Remote(
            command_executor=_browserstack_url(),
            desired_capabilities=desired_cap
        )

    if request.param == "RemoteFirefox":
        desired_cap = {
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1920x1080',
            'browser': 'Firefox',
            'browser_version': 'latest',
            'name': "FirefoxTesting",
            'browserstack.local': 'true',
            'build': 'Test Build Firefox',
        }
        driver = webdriver.Remote(
            command_executor=_browserstack_url(),
            desired_capabilities=desired_cap
        )

    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def init_driver_class(request, init_driver):
    request.cls.driver = init_driver
