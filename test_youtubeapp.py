import unittest
from appium import webdriver
import time
import warnings


class TestNativeApp(unittest.TestCase):
    def setUp(self):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "Xperia",
            "appPackage": "com.google.android.youtube",
            "appActivity": "com.google.android.apps.youtube.app.WatchWhileActivity",
            "unicodeKeyboard": True,
        }

        warnings.filterwarnings(
            action="ignore", message="unclosed", category=ResourceWarning
        )

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", capabilities)
        self.driver.implicitly_wait(5000)

    def tearDown(self):
        self.driver.quit()

    def test_Mariusz(self):
        lupa = self.driver.find_element_by_accessibility_id("Szukaj")

        lupa.click()

        pole_szukaj = self.driver.find_element_by_id(
            "com.google.android.youtube:id/search_edit_text"
        )

        pole_szukaj.send_keys("tanio skóry nie sprzedam")

        self.driver.press_keycode(66)

        propozycje = self.driver.find_elements_by_class_name("android.view.ViewGroup")

        propozycje_tytul = [p.get_attribute("name") for p in propozycje]
        print(propozycje_tytul)

        licz_mariusz = len(
            [
                p.get_attribute("name")
                for p in propozycje
                if p.get_attribute("name").startswith("Mariusz")
            ]
        )

        time.sleep(3)

        self.assertGreaterEqual(licz_mariusz, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
