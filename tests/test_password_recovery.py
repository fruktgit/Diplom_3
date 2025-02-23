import allure
from data import generate_user_data

from curl import Urls
from pages.main_page import MainPage
from pages.recovery_password_page import PasswordRecoveryPage

@allure.suite('Восстановление пароля')

class TestRecoveryPassword:

    @allure.title('Проверка на переход по клику на Восстановить пароль на странице логина')
    def test_click_logo_button_go_to_home(self, driver):
        MainPage(driver).click_on_account()
        PasswordRecoveryPage(driver).click_password_reset_link()
        assert driver.current_url == Urls.url_restore

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_reset(self, driver):
        user_data = generate_user_data()
        main_page = MainPage(driver)
        recovery_page = PasswordRecoveryPage(driver)

        main_page.go_to_site(Urls.url_restore)
        recovery_page.set_email_for_reset_password(user_data["email"])
        recovery_page.click_reset_button()
        recovery_page.find_save_button()

        assert recovery_page.current_url() == Urls.url_reset

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_make_field_active(self, driver):
        user_data = generate_user_data()
        main_page = MainPage(driver)
        recovery_page = PasswordRecoveryPage(driver)

        main_page.go_to_site(Urls.url_restore)
        recovery_page.set_email_for_reset_password(user_data["email"])
        recovery_page.click_reset_button()
        recovery_page.find_save_button()
        recovery_page.click_on_show_password_button()
        assert recovery_page.find_input_active()