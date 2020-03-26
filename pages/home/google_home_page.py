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
        self.keyboard_enter('name', self._google_search_field_name, search_param)

    def fetch_all_links(self):
        return self.get_element('css', self._links_google_search_page)

    def enter_email(self, email):
        self.clear_field('id', self._tb_login_email)
        self.enter_data_into_text_field('id', self._tb_login_email, email)

    def enter_password(self, password):
        self.clear_field('id', self._tb_login_password)
        self.enter_data_into_text_field('id', self._tb_login_password, password)

    def click_sign_in_button(self):
        self.element_click('xpath', self._btn_sign_in)

    def valid_login(self, username, password):
        self.enter_email(username)
        self.enter_password(password)
        self.click_sign_in_button()
        element = self.is_element_present('xpath', self._icon_user_profile)
        return element

    def validate_home_page_title(self, username, password):
        self.enter_email(username)
        self.enter_password(password)
        self.click_sign_in_button()
        page_title = self.validate_page_title()
        return page_title

    def invalid_login(self, username, password):
        self.enter_email(username)
        self.enter_password(password)
        self.click_sign_in_button()
        element = self.is_element_present('xpath', self._msg_invalid_login)
        return element

    def sign_out(self):
        self.wait_till_circle_disappears()
        self.element_click('css', self._link_user_settings_css)
        self.wait_till_element_appears('css', self._link_sign_out_css)
        self.element_click('css', self._link_sign_out_css)

    def save_screenshot(self, message):
        self.take_screenshots(message)
