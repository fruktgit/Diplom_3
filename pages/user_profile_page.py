import allure

from locators import UserProfileLocators
from pages.base_page import BasePage


class UserProfilePage(BasePage):

    @allure.step('Проверяем переход на страницу профиля')
    def check_switch_on_profile(self) -> object:
        self.find_element(UserProfileLocators.PROFILE_BUTTON)
        return self.current_url()

    @allure.step('Нажимаем кнопку «История заказов»')
    def click_order_history_button(self):
        self.wait_clickable(UserProfileLocators.ORDER_HISTORY_BUTTON)
        self.find_element(UserProfileLocators.ORDER_HISTORY_BUTTON).click()

    @allure.step('Проверяем переход на страницу История заказов')
    def check_switch_on_order_history(self):
        self.find_element(UserProfileLocators.ENABLED_ORDER_HISTORY_BUTTON)
        return self.current_url()

    @allure.step('Нажимаем кнопку «Выход»')
    def click_log_out_button(self):
        self.find_element(UserProfileLocators.LOGOUT_BUTTON).click()

