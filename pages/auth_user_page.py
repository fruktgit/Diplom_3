import allure
from locators import MainPageLocators, AuthLoginLocators
from pages.base_page import BasePage


class AuthUserPage(BasePage):

    @allure.step('Перейти на страницу авторизации по кнопке "Войти в аккаунт"')
    def click_personal_account_button(self):
        self.find_element(MainPageLocators.LOGIN_PROFILE_BUTTON).click()

    @allure.step('Заполняем поле "email"')
    def set_email_field(self, user_email):
        self.find_element(AuthLoginLocators.EMAIL_FIELD).send_keys(user_email)


    @allure.step('Заполняем поле "Пароль"')
    def set_password_field(self, user_password):
        self.find_element(AuthLoginLocators.PASSWORD_FIELD).send_keys(user_password)

    @allure.step('Нажимаем кнопку «Войти»')
    def click_login_button(self):
        self.find_element(AuthLoginLocators.LOGIN_BUTTON_ANY_FORMS).click()

    @allure.step('Авторизация')
    def login(self, user_login, user_password):
        self.click_personal_account_button()
        self.set_email_field(user_login)
        self.set_password_field(user_password)
        self.click_login_button()

    @allure.step('Проверяем переход на страницу Авторизации')
    def check_switch_on_login_page(self):
        self.find_element(AuthLoginLocators.LOGIN_TEXT)
        return self.current_url()
