class googlepage:
    
    def __init__(self, driver):
        self.driver = driver
        self.search_field_name = 'q'
        self.link_class_name = 'r'
        self.results = []
        self.driver.get('https://www.google.com/xhtml')
        
    
    def submit_search(self, search):
        self.search_field = self.driver.find_element_by_name(self.search_field_name)
        self.search_field.clear()
        self.search_field.send_keys(search)
        self.search_field.submit()



    def get_all_links(self):
        self.links = self.driver.find_elements_by_class_name(self.link_class_name)
        for link in self.links: 
            self.results.append(link.text)
