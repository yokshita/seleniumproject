import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driverinit(request):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("driverinit")
class BaseTest:
    pass


class Test_Selenium(BaseTest):

    def test_one(self):
        self.driver.get("https://www.python.org/")
        print(f'title={self.driver.title}')
        assert "Python" in self.driver.title