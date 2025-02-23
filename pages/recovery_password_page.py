import allure
from locators import AuthForgotPasswordlocators, AuthLoginLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):

    @allure.step('Нажать на "Восстановить пароль"')
    def click_password_reset_link(self):
        self.find_element(AuthLoginLocators.FORGOT_PASSWORD).click()

    @allure.step('Вводим емейл в поле для восстановления пароля')
    def set_email_for_reset_password(self, email):
        self.find_element(AuthForgotPasswordlocators.INPUT_EMAIL).send_keys(email)

    @allure.step('Нажимаем на кнопку Восстановить')
    def click_reset_button(self):
        return self.find_element(AuthForgotPasswordlocators.RESET_BUTTON).click()

    @allure.step('Кликаем на кнопку Показать/скрыть пароль')
    def click_on_show_password_button(self):
        self.find_element(AuthForgotPasswordlocators.SHOW_PASSWORD_BUTTON).click()

    @allure.step('Найти кнопку Сохранить')
    def find_save_button(self):
        self.find_element(AuthForgotPasswordlocators.SAVE_BUTTON)

    @allure.step('Найти активное поле Пароль')
    def find_input_active(self):
        return self.find_element(AuthForgotPasswordlocators.INPUT_ACTIVE)
