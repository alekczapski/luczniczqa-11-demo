import unittest
from appium import webdriver
import time
import warnings


class TestWebApp(unittest.TestCase):
    def setUp(self):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "Xperia",
            "browserName": "Chrome",
        }

        warnings.filterwarnings(
            action="ignore", message="unclosed", category=ResourceWarning
        )

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        # Navigate to the page and interact with the elements on the guinea-pig page using id.
        self.driver.get("http://saucelabs.com/test/guinea-pig")
        div = self.driver.find_element_by_id("i_am_an_id")

        # check the text retrieved matches expected value
        self.assertEqual("I am a div", div.text)

        # populate the comments field by id
        self.driver.find_element_by_id("comments").send_keys("My comment")

        time.sleep(3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
