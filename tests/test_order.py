import allure
import pytest

from config import API_ENDPOINTS
from pages.auth_user_page import AuthUserPage
from pages.main_page import MainPage

from locators import OrdersPageLocators
from pages.order_page import CreateOrderPage
from pages.user_profile_page import UserProfilePage

@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite('Лента заказов')
class TestCreateOrder:
    @allure.title('Проверка появления всплывающего окна с деталями при клике на заказ')
    def test_get_order_popup(self, driver):
        mainpage = MainPage(driver)
        createorder = CreateOrderPage(driver)

        mainpage.click_orders_list_button()
        createorder.click_order()
        assert createorder.check_order_structure() == True

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_find_order_in_list(self, driver, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения
        mainpage = MainPage(driver)
        userpage = AuthUserPage(driver)
        userprofile = UserProfilePage(driver)
        createorder = CreateOrderPage(driver)


        client.post(API_ENDPOINTS["create_user"], user_data)
        userpage.login(user_data["email"], user_data["password"])

        mainpage.click_on_account()
        mainpage.click_constructor_button()

        mainpage.add_filling_to_order()
        mainpage.click_order_button()
        mainpage.check_show_window_with_order_id()
        order_number = mainpage.get_with_order_id()
        mainpage.click_close_modal_order()
        mainpage.click_on_account()
        userprofile.click_order_history_button()
        is_order_id_found_at_history = createorder.is_order_id_found_at_history(order_number)
        mainpage.click_orders_list_button()
        is_order_id_found_at_feed = createorder.is_order_id_found_at_feed(order_number)
        assert is_order_id_found_at_history and is_order_id_found_at_feed

    @allure.title('При создании заказа, происходит увеличения значения счетчиков заказов "Выполнено за все время"/"Выполнено за сегодня"')

    @pytest.mark.parametrize('counter', [OrdersPageLocators.TOTAL_ORDER_COUNT, OrdersPageLocators.DAILY_ORDER_COUNT])
    def test_today_orders_counter(self, driver, setup_and_teardown, counter):
        client, user_data = setup_and_teardown  # Распаковываем значения
        mainpage = MainPage(driver)
        userpage = AuthUserPage(driver)
        createorder = CreateOrderPage(driver)

        client.post(API_ENDPOINTS["create_user"], user_data)
        userpage.login(user_data["email"], user_data["password"])

        mainpage.click_on_account()

        mainpage.click_orders_list_button()
        prev_counter_value = createorder.get_total_order_count_daily(counter)
        mainpage.click_constructor_button()
        mainpage.add_filling_to_order()
        mainpage.click_order_button()
        mainpage.click_close_modal_order()
        mainpage.click_orders_list_button()
        current_counter_value = createorder.get_total_order_count_daily(counter)
        assert current_counter_value > prev_counter_value

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    def test_new_order_appears_in_work_list(self, driver, setup_and_teardown):
        client, user_data = setup_and_teardown  # Распаковываем значения
        mainpage = MainPage(driver)
        userpage = AuthUserPage(driver)
        createorder = CreateOrderPage(driver)

        client.post(API_ENDPOINTS["create_user"], user_data)
        userpage.login(user_data["email"], user_data["password"])

        mainpage.add_filling_to_order()
        mainpage.click_order_button()
        order_number = mainpage.get_with_order_id()
        mainpage.click_close_modal_order()
        mainpage.click_orders_list_button()
        order_number_refactor = createorder.get_user_order(order_number)
        order_in_progress = createorder.get_user_order_in_progress()
        assert order_number_refactor == order_in_progress
