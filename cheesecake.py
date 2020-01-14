# import von selenium und unittest module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


# erstellen der klasse die von unittest.testcase erbt
class GoogleTest(unittest.TestCase):
    def setUp(self):
        # setup vom chrome browser vor jedem test
        self.driver = webdriver.Chrome()

    def test_google_search(self):
        # automatisieren der googlesuche
        self.driver.get('https://www.google.com/xhtml')
        search_field = self.driver.find_element_by_name('q')
        search_field.send_keys('cheesecake')
        search_field.submit()

        time.sleep(5)

        # suchergebnisse der ersten seite
        links = self.driver.find_elements_by_class_name('r')
        
        # speichern der ergebnisse in results
        results = []
        for link in links: 
            results.append(link.text)

        # test der ersten 3 ergebnisse auf cheesecake
        for result in results[:3]:
            assert "cheesecake" in result.lower()
    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

