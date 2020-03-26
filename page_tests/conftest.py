from base.web_driver_factory import WebDriverFactory
import pytest

@pytest.yield_fixture()
def setup():
    print("Running Setup")
    yield
    print("After running setup")

@pytest.yield_fixture(scope="class")
def onetime_setup(request, browser):

    # get driver instance as per the browser chosen in the command line : ex: Firefox, Chrome, Ie an Safari
    driver_instance = WebDriverFactory(browser)
    driver = driver_instance.get_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType")

@pytest.yield_fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.yield_fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")
