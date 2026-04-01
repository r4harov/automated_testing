class BaseComponent:

    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

    def find_element(self):
        return self.page.find_element(self.locator)

    def get_text(self):
        return str(self.find_element().text)