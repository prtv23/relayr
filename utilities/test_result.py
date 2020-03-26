from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class TestResult(SeleniumDriver):

    def __init__(self, driver):
        super(TestResult, self).__init__(driver)

    # instance to logger class
    log = cl.custom_log(logging.DEBUG)
    # list to store the test status
    test_status_list = []

    def test_status(self, result, result_message):

        if result is not None:
            if result:
                self.test_status_list.append(True)
                self.log.info(str(result)+" "+"added into the list"+result_message)

            else:
                self.test_status_list.append(False)
                self.log.info(str(result)+" "+"added into the list"+result_message)
                self.take_screenshots(result_message)
        else:
            self.log.error("No result was available"+result_message)
            self.take_screenshots(result_message)

    def mark(self, result, result_message):
        self.test_status(result, result_message)

    def mark_final(self, result, result_message):
        self.test_status(result, result_message)
        print("*"*20)
        print(self.test_status_list)
        if False in self.test_status_list:
            # clears the list values
            self.test_status_list.clear()
            return False
        else:
            # clears the list values
            self.test_status_list.clear()
            return True
