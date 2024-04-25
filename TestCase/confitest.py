import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()  # Or any other webdriver you're using
    return driver

# Hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.metadata['Project Name'] = 'nop Commerce'
    config.metadata['Module Name'] = 'Customers'
    config.metadata['Tester'] = 'Darshan'

# Hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
