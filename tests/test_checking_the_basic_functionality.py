import allure
import pytest
from curl import Urls
from config import API_ENDPOINTS
from pages.main_page import MainPage
from pages.auth_user_page import AuthUserPage

@pytest.mark.usefixtures("setup_and_teardown")

@allure.suite('Проверка основного функционала')
class TestMainPage:

    @allure.title('переход по клику на «Конструктор»')
    def test_go_to_constructor(self, driver):


        MainPage(driver).click_constructor_button()
        current_url = MainPage(driver).current_url()
        assert current_url == Urls.main_site

    @allure.title('переход по клику на «Лента заказов»')
    def test_redirection_to_order_list(self, driver, setup_and_teardown):
        self.client.post(API_ENDPOINTS["create_user"], self.user_data)
        user_data = self.user_data
        AuthUserPage(driver).login(user_data["email"], user_data["password"])

        MainPage(driver).click_on_account()

        MainPage(driver).click_orders_list_button()
        current_url = MainPage(driver).current_url()
        assert current_url == Urls.url_feed

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_popup_of_ingredient(self, driver, setup_and_teardown):
        self.client.post(API_ENDPOINTS["create_user"], self.user_data)
        user_data = self.user_data
        AuthUserPage(driver).login(user_data["email"], user_data["password"])

        MainPage(driver).click_on_account()
        MainPage(driver).click_constructor_button()


        MainPage(driver).click_on_ingredient()
        actually_text = MainPage(driver).check_show_window_with_details()
        assert actually_text == "Детали ингредиента"

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details_window(self, driver, setup_and_teardown):
        self.client.post(API_ENDPOINTS["create_user"], self.user_data)
        user_data = self.user_data
        AuthUserPage(driver).login(user_data["email"], user_data["password"])

        MainPage(driver).click_on_account()
        MainPage(driver).click_constructor_button()


        MainPage(driver).click_on_ingredient()
        MainPage(driver).click_cross_button()
        MainPage(driver).invisibility_ingredient_details()
        assert MainPage(driver).check_displayed_ingredient_details() == False

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_ingredient_counter(self, driver, setup_and_teardown):
        prev_counter_value = MainPage(driver).get_count_value()
        MainPage(driver).add_filling_to_order()
        actual_value = MainPage(driver).get_count_value()
        assert actual_value > prev_counter_value

    @allure.title('Проверка возможности оформления заказ авторизованным пользователем')
    @allure.description('Нажимаем кнопку «Оформить заказ» и проверяем, что заказ оформлен и появился идентификатор заказа')
    def test_successful_order(self, driver, setup_and_teardown):
        self.client.post(API_ENDPOINTS["create_user"], self.user_data)
        user_data = self.user_data
        AuthUserPage(driver).login(user_data["email"], user_data["password"])

        MainPage(driver).click_on_account()
        MainPage(driver).click_constructor_button()


        MainPage(driver).add_filling_to_order()
        MainPage(driver).click_order_button()
        actually_text = MainPage(driver).check_show_window_with_order_id()
        assert actually_text == "идентификатор заказа" and MainPage(driver).check_displayed_order_status_text() == True
