from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SwagLabs(BasePage):
    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
            print('Иконка найдена')
            return True
        except NoSuchElementException:
            print('Иконка не найдена')
            return False

    def exist_username(self):
        try:
            self.find_element(locator='#user-name')
            print('Поле Имя найдено')
            return True
        except NoSuchElementException:
            print('Поле Имя не найдено')
            return False

    def exist_password(self):
        try:
            self.find_element(locator='#password')
            print('Поле Пароль найдено')
            return True
        except NoSuchElementException:
            print('Поле Пароль не найдено')
            return False
