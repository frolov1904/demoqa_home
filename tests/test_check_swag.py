from pages.swag_labs import SwagLabs


def test1(browser):
    demo_page = SwagLabs(browser)
    demo_page.visit()
    assert demo_page.exist_icon()


def test2(browser):
    demo_page = SwagLabs(browser)
    demo_page.visit()
    assert demo_page.exist_username()


def test3(browser):
    demo_page = SwagLabs(browser)
    demo_page.visit()
    assert demo_page.exist_password()
