import allure
import pytest
from config import API_ENDPOINTS
from curl import Urls
from pages.main_page import MainPage
from pages.auth_user_page import AuthUserPage
from pages.base_page import BasePage
from pages.user_profile_page import UserProfilePage


@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite('Личный кабинет ')
class TestLKProfile:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_account_from_header(self, driver, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения

        client.post(API_ENDPOINTS["create_user"], user_data)
        AuthUserPage(driver).login(user_data["email"], user_data["password"])

        MainPage(driver).click_on_account()
        current_url = UserProfilePage(driver).check_switch_on_profile()
        assert current_url == Urls.url_profile

    @allure.title('переход в раздел «История заказов»')
    def test_go_to_order_history(self, driver, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения

        client.post(API_ENDPOINTS["create_user"], user_data)
        AuthUserPage(driver).login(user_data["email"], user_data["password"])

        MainPage(driver).click_on_account()

        UserProfilePage(driver).click_order_history_button()
        current_url = UserProfilePage(driver).check_switch_on_order_history()
        assert current_url == Urls.url_profile_order_history

    @allure.title('выход из аккаунта')
    @allure.description('выход из аккаунта')
    def test_logout(self, driver, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения

        client.post(API_ENDPOINTS["create_user"], user_data)
        AuthUserPage(driver).login(user_data["email"], user_data["password"])

        MainPage(driver).click_on_account()
        UserProfilePage(driver).click_log_out_button()
        current_url = AuthUserPage(driver).check_switch_on_login_page()
        assert current_url == Urls.url_login
