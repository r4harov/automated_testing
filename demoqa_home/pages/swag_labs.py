from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element('div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def exist_username(self):
        try:
            self.find_element('#user-name')
        except NoSuchElementException:
            return False
        return True

    def exist_password(self):
        try:
            self.find_element('#password')
        except NoSuchElementException:
            return False
        return True