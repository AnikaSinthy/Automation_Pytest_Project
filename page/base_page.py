from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class BasePage():
    def __init__(self):
        self.driver = driver

    def get_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def click_element(self, locator):
        self.get_element(locator).click()

    def click_element_by_mouse(self, locator):
        action = ActionChains(self.driver)
        element = self.get_element(locator)
        action.move_to_element(element).click().perform()

    def enter_at(self, locator, data):
        self.get_element(locator).send_keys(data)

    def is_selected(self, locator):
        return self.get_element(locator).is_selected()

    def select_by_value(self, locator, value):
        select = Select(self.get_element(locator))
        select.select_by_index(value)

    def select_by_index(self, locator, index):
        select = Select(self.get_element(locator))
        select.select_by_index(index)

    def switch_to_active_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def drag_and_drop(self, source_location, destination_location):
        drag = self.get_element(source_location)
        drop = self.get_element(destination_location)
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()

    def switch_to_iframe(self, locator):
        self.driver.switch_to.frame(self.get_element(locator))

