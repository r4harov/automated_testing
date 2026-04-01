from pages.base_page import BasePage
from components.base_component import BaseComponent


def test_footer_text(driver):
    page = BasePage(driver, 'https://demoqa.com/')
    page.visit()

    footer = BaseComponent(page, 'footer')
    text = footer.get_text()

    assert 'TOOLSQA.COM' in text


def test_center_text(driver):
    page = BasePage(driver, 'https://demoqa.com/')
    page.visit()

    page.driver.get("https://demoqa.com/elements")

    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    element = WebDriverWait(page.driver, 5).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Please select an item from left')]")
        )
    )

    text = element.text

    assert text == 'Please select an item from left to start practice.'