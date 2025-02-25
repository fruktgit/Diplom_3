import allure
from pages.base_page import BasePage
from locators import MainPageLocators, OrdersPageLocators


class MainPage(BasePage):
    @allure.step('Перейти в "ЛК" по кнопке "Личный кабинет"')
    def click_on_account(self):
        self.move_and_click(MainPageLocators.PROFILE_BUTTON)

    @allure.step('Переход на страницу Лента заказов')
    def click_orders_list_button(self):
        self.move_and_click(MainPageLocators.ORDERS_LIST_BUTTON)
        self.wait_element_visibility(OrdersPageLocators.ORDERS_LIST_TITLE)

    @allure.step('Переход в "Конструктор"')
    def click_constructor_button(self):
        self.move_and_click(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.wait_element_visibility(MainPageLocators.MAIN_LIST_TITLE)


    @allure.step('Кликаем на ингредиент')
    def click_on_ingredient(self):
        self.wait_clickable(MainPageLocators.BUN_INGREDIENT)
        self.find_element(MainPageLocators.BUN_INGREDIENT).click()

    @allure.step('Проверяем, что появилось всплывающее окно с деталями игридиента')
    def check_show_window_with_details(self):
        self.wait_element_visibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)
        return self.find_element(MainPageLocators.INGREDIENT_DETAILS_POPUP).text

    @allure.step('Закрываем попап крестиком')
    def click_cross_button(self):
        self.move_and_click(MainPageLocators.CROSS_BUTTON)

    @allure.step('Проверить скрытость деталей ингредиентов')
    def invisibility_ingredient_details(self):
        self.check_invisibility(MainPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Проверить наличие деталей ингредиентов на экране')
    def check_displayed_ingredient_details(self) -> bool:
        return self.check_presense(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    @allure.step('Получаем значение счетчика ингредиента')
    def get_count_value(self):
        return self.find_element(MainPageLocators.INGREDIENT_COUNTER).text

    @allure.step('Добавить ингридиент в заказ')
    def add_filling_to_order(self):
        self.wait_clickable(MainPageLocators.BUN_INGREDIENT)
        self.drag_and_drop_on_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.ORDER_BASKET)

    @allure.step('Нажать на кнопку Оформить заказ')
    def click_order_button(self):
        self.move_and_click(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Проверяем, что заказ оформлен и появился идентификатор заказа')
    def check_show_window_with_order_id(self):
        self.wait_element_visibility(MainPageLocators.ORDER_IDENTIFICATE)
        return self.find_element(MainPageLocators.ORDER_IDENTIFICATE).text

    @allure.step('Получение ORDER_ID')
    def get_with_order_id(self):
        self.wait_element_visibility(MainPageLocators.ORDER_IDENTIFICATE)
        order_id = self.find_element(MainPageLocators.ORDER_ID).text
        while order_id == '9999':
            order_id = self.find_element(MainPageLocators.ORDER_ID).text
        return f"{order_id}"


    @allure.step('Проверить наличие, что заказа начали готовить')
    def check_displayed_order_status_text(self) -> bool:
        return self.check_presense(MainPageLocators.ORDER_STATUS_TEXT).is_displayed()

    @allure.step("Закрыть модальное окно после создания заказа")
    def click_close_modal_order(self):
        self.wait_element_visibility(MainPageLocators.CLOSE_MODAL_ORDER)
        self.click_on_element(MainPageLocators.CLOSE_MODAL_ORDER)
