# import von selenium und unittest module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import os
from pom_google_homepage import googlepage


# erstellen der klasse die von unittest.testcase erbt
class GoogleTest(unittest.TestCase):
    def setUp(self):
        # setup vom chrome browser vor jedem test
        self.driver = webdriver.Chrome()
       

    def test_google_search(self):
        # automatisieren der googlesuche
        keyword = 'cheesecake'
        search = googlepage(self.driver)
        search.submit_search(keyword)
        time.sleep(5)

        # suchergebnisse der ersten seite
        search.get_all_links()

        assert len(search.results) > 0, "No results found"
        
        # test der ersten 3 ergebnisse auf cheesecake
        for result in search.results[:3]:
            assert "cheesecake" in result.lower()
    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

