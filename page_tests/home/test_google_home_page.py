from pages.home.google_home_page import GooglePage
from utilities.test_result import TestResult
from data.google_page_data import GooglePageData as Data
import pytest
import unittest


@pytest.mark.usefixtures("onetime_setup", "setup")
class SearchTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = GooglePage(self.driver)
        self.TS = TestResult(self.driver)

    @pytest.mark.run(order=1)
    def test_validate_search_field_presence(self):
        tc_res = self.lp.verify_search_field_presence()
        assert True == tc_res

    @pytest.mark.run(order=2)
    def test_validate_search_text_enter(self):
        tc_res = self.lp.enter_data_into_search_field(Data.search_input)
        assert True == tc_res

    @pytest.mark.run(order=3)
    def test_validate_search_results(self):
        web_elements = self.lp.fetch_all_links()
        for element in web_elements:
            search_input = Data.search_input.lower()
            search_res = element.text.lower()

            tc_res = search_input in search_res
            assert True == tc_res

