from pages.swag_labs import SwagLabs


def test_icon(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_icon()


def test_username(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_username()


def test_password(driver):
    page = SwagLabs(driver)
    page.visit()
    assert page.exist_password()