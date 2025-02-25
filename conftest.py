import allure
import pytest
from selenium import webdriver
from config import API_ENDPOINTS
from api_client import APIClient
from data import generate_user_data
from curl import Urls


@allure.step('Открытие браузера: {browser}')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = request.param  # Получаем имя браузера

    options = webdriver.ChromeOptions() if request.param == 'chrome' else webdriver.FirefoxOptions()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options) if request.param == 'chrome' else webdriver.Firefox(options=options)
    driver.set_window_size(1200, 800)
    driver.get(Urls.main_site)

    # Записываем браузер в отчет
    allure.attach(browser, name="Браузер", attachment_type=allure.attachment_type.TEXT)

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def setup_and_teardown():
    """
        Фикстура для подготовки данных перед тестом и их очистки после теста.
        """
    client = APIClient()
    user_data = generate_user_data()

    yield client, user_data  # Возвращаем объект APIClient и тестовые данные

    # Удаление созданного курьера после теста
    response = client.post(API_ENDPOINTS["login_user"], data={
        "email": user_data["email"],
        "password": user_data["password"]
    })
    if response.status_code == 200:
        token = response.json()["accessToken"]
        client.delete(API_ENDPOINTS["login_user"], headers={'Authorization': f'{token}'})