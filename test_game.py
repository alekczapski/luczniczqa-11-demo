import unittest
from appium import webdriver
import warnings


class TestGame(unittest.TestCase):
    def setUp(self):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "Xperia",
            "appPackage": "air.com.amanitadesign.chuchel.gp",
            "appActivity": "air.com.amanitadesign.chuchel.gp.AppEntry",
        }

        warnings.filterwarnings(
            action="ignore", message="unclosed", category=ResourceWarning
        )

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
        self.driver.update_settings({"imageMatchThreshold": 0.8})
        self.driver.implicitly_wait(5000)

    def tearDown(self):
        self.driver.quit()

    def test_laczek(self):
        ptak = self.driver.find_element_by_image("chuchel/ptak.png")
        ptak.click()
        laczki = self.driver.find_elements_by_image("chuchel/laczek.png")
        print("\nIlość laczków: " + str(len(laczki)))
        self.assertTrue(len(laczki) == 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
