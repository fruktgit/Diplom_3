import allure
from selenium.webdriver import ActionChains

from curl import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def click_on_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)
    @allure.step('Ждем элемент')
    def wait_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(locator))

    def wait_element_visibility(self, locator):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))

    def check_invisibility(self, locator) -> object:
        return WebDriverWait(self.driver, 10).until(ec.invisibility_of_element(locator))


    def check_presense(self, locator):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def move_and_click(self, locator, timeout=30):
        """Ожидает появления элемента и кликает по нему."""
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(ec.element_to_be_clickable(locator))

        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)

        drag_and_drop_script = """
              function simulateDragDrop(sourceNode, destinationNode) {
                  var event = document.createEvent('HTMLEvents');
                  event.initEvent('dragstart', true, true);
                  sourceNode.dispatchEvent(event);

                  var dropEvent = document.createEvent('HTMLEvents');
                  dropEvent.initEvent('drop', true, true);
                  destinationNode.dispatchEvent(dropEvent);

                  var dragEndEvent = document.createEvent('HTMLEvents');
                  dragEndEvent.initEvent('dragend', true, true);
                  sourceNode.dispatchEvent(dragEndEvent);
              }
              simulateDragDrop(arguments[0], arguments[1]);
          """
        self.driver.execute_script(drag_and_drop_script, draggable, droppable)

    @allure.step('Перейти по адресу')
    def go_to_site(self, url=None):
        if url is None:
            url = Urls.main_site
        self.driver.get(url)

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url

    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(ec.presence_of_all_elements_located(locator))

    def wait_for_text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 15).until(ec.text_to_be_present_in_element(locator, text))

    def get_actually_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text