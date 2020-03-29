from base.selenium_driver import SeleniumDriver


class GooglePage(SeleniumDriver):

    # locators
    _google_search_field_name = "q"
    _links_google_search_page = "a>h3"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_search_field_presence(self):
        return self.is_element_present('name', self._google_search_field_name)

    def enter_data_into_search_field(self, search_param):
        return self.keyboard_enter('name', self._google_search_field_name, search_param)

    def fetch_all_links(self):
        return self.get_element('css', self._links_google_search_page)