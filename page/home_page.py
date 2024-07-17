import os
import time

from locators.locators import Locators
from page.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators

    def click_autocomplete(self):
        self.click_element(self.locator.AutoComplete)
        time.sleep(2)

    def enter_address(self, address):
        self.enter_at(self.locator.Address, address)

    def enter_street_address(self, street_address):
        self.enter_at(self.locator.Street_address, street_address)

    def enter_street_address_2(self, street_address_2):
        self.enter_at(self.locator.Street_address_2, street_address_2)

    def enter_city(self, city):
        self.enter_at(self.locator.City, city)

    def enter_state(self, state):
        self.enter_at(self.locator.State, state)

    def enter_zip_code(self, zip_code):
        self.enter_at(self.locator.Zip_Code, zip_code)

    def enter_country(self, country):
        self.enter_at(self.locator.Country, country)

    def click_buttons(self):
        self.click_element(self.locator.Buttons)
        time.sleep(2)

    def click_primary(self):
        self.click_element(self.locator.PrimaryButton)
        time.sleep(1)

    def click_success(self):
        self.click_element(self.locator.SuccessButton)
        time.sleep(1)

    def click_info(self):
        self.click_element(self.locator.InfoButton)
        time.sleep(1)

    def click_warning(self):
        self.click_element(self.locator.WarningButton)
        time.sleep(1)

    def click_danger(self):
        self.click_element(self.locator.DangerButton)
        time.sleep(1)

    def click_link(self):
        self.click_element(self.locator.LinkButton)
        time.sleep(1)

    def click_left(self):
        self.click_element(self.locator.LeftButton)
        time.sleep(1)

    def click_middle(self):
        self.click_element(self.locator.MiddleButton)
        time.sleep(1)

    def click_right(self):
        self.click_element(self.locator.RightButton)
        time.sleep(1)

    def click_one_button(self):
        self.click_element(self.locator.OneButton)
        time.sleep(1)

    def click_two_button(self):
        self.click_element(self.locator.TwoButton)
        time.sleep(1)

    def click_drop_down(self):
        self.click_element(self.locator.Drop_down)
        time.sleep(1)

    def click_drop_down_link1(self):
        self.click_element(self.locator.Drop_down_link_1)

    def click_drop_down_link2(self):
        self.click_element(self.locator.Drop_down_link_2)

    def click_checkbox(self):
        self.click_element(self.locator.CheckBox)
        time.sleep(2)

    def select_checkboxes_checkbox1(self):
        self.click_element(self.locator.Checkbox1)

    def assert_checkboxes_checkbox1(self):
        value = self.is_selected(self.locator.Checkbox1)
        print(value)
        return value

    def select_checkboxes_checkbox2(self):
        self.click_element(self.locator.Checkbox2)

    def assert_checkboxes_checkbox2(self):
        value = self.is_selected(self.locator.Checkbox2)
        print(value)
        return value

    def select_checkboxes_checkbox3(self):
        self.click_element(self.locator.Checkbox3)

    def assert_checkboxes_checkbox3(self):
        value = self.is_selected(self.locator.Checkbox3)
        print(value)
        return value

    def select_checkboxes(self):
        self.click_element(self.locator.Checkbox1)
        self.click_element(self.locator.Checkbox2)
        time.sleep(5)

    def assert_checkboxes(self):
        value_1 = self.is_selected(self.locator.Checkbox1)
        value_2 = self.is_selected(self.locator.Checkbox2)
        print (value_1,value_2)
        return (value_1 , value_2)

    def click_datepicker(self):
        self.click_element(self.locator.Datepicker)

    def click_date(self):
        self.click_element(self.locator.Date)

    def enter_date(self, date):
        self.enter_at(self.locator.Date, date)

    def click_drop(self):
        self.click_element(self.locator.DropDown)

    def click_down(self):
        self.click_element(self.locator.DropDownButton)

    def click_check_box(self):
        self.click_element(self.locator.check_box)

    def click_enable(self):
        self.click_element(self.locator.Enabled_and_disable_element)

    def click_input(self):
        self.click_element(self.locator.inputHere)

    def enter_input(self, input):
        self.enter_at(self.locator.inputHere, input)

    def click_file(self):
        self.click_element(self.locator.FileUpload)

    def image_upload(self):
        directory = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "image/Screenshot (1).png"))
        self.enter_at(self.locator.choose, directory)

    def click_key(self):
        self.click_element(self.locator.key_and_mouse_press)

    def click_name(self):
        self.click_element(self.locator.full_name)

    def enter_name(self, name):
        self.enter_at(self.locator.full_name, name)

    def click_button(self):
        # self.click_element(self.locator.button_name)
        self.click_element_by_mouse(self.locator.button_name)

    def click_modal(self):
        self.click_element(self.locator.Modal)

    def click_open(self):
        self.click_element(self.locator.OpenModel)

    def click_close(self):
        self.click_element(self.locator.CloseButton)

    def click_page(self):
        self.click_element(self.locator.PageScroll)

    def click_fullname(self):
        self.click_element(self.locator.FullName)

    def enter_fullname(self, name):
        self.enter_at(self.locator.FullName, name)

    def click_birth(self):
        self.click_element(self.locator.date)

    def enter_birth(self, date):
        self.enter_at(self.locator.date, date)

    def click_radiobutton(self):
        self.click_element(self.locator.RadioButton)

    def select_radiobutton_radiobutton1(self):
        self.click_element(self.locator.RadioButton1)

    def assert_radiobutton1_selected(self):
        value = self.is_selected(self.locator.RadioButton1)
        print(value)
        return value

    def select_radiobutton_radiobutton2(self):
        self.click_element(self.locator.RadioButton2)

    def assert_radiobutton2_selected(self):
        value = self.is_selected(self.locator.RadioButton2)
        print(value)
        return value

    def select_radiobutton_radiobutton3(self):
        self.click_element(self.locator.RadioButton3)

    def assert_radiobutton3_selected(self):
        value = self.is_selected(self.locator.RadioButton3)
        print(value)
        return value

    def click_switch(self):
        self.click_element(self.locator.SwitchWindow)

    def click_tab(self):
        self.click_element(self.locator.OpenNewTab)

    def click_alert(self):
        self.click_element(self.locator.OpenAlert)

    def click_web(self):
        self.click_element(self.locator.CompleteWebForm)

    def click_firstname(self):
        self.click_element(self.locator.FirstName)

    def enter_firstname(self, name_1):
        self.enter_at(self.locator.FirstName, name_1)

    def click_lastname(self):
        self.click_element(self.locator.LastName)

    def enter_lastname(self, name_2):
        self.enter_at(self.locator.LastName, name_2)

    def click_job(self):
        self.click_element(self.locator.Job_title)

    def enter_job(self, job):
        self.enter_at(self.locator.Job_title, job)

    def select_web_high_school(self):
        self.click_element(self.locator.HighSchool)

    def select_web_college(self):
        self.click_element(self.locator.College)

    def select_web_grand(self):
        self.click_element(self.locator.GrabSchool)

    def select_web_male(self):
        self.click_element(self.locator.Male)

    def select_web_female(self):
        self.click_element(self.locator.Female)

    def select_web_not_prefer(self):
        self.click_element(self.locator.Not_prefer)

    def select_number(self):
        self.select_by_value(self.locator.Experience, "1")

    def click_date_1(self):
        self.click_element(self.locator.date_1)

    def enter_date_1(self, date):
        self.enter_at(self.locator.date_1, date)

    def click_submit_button(self):
        self.click_element(self.locator.Click_on_submit_button)

    def click_on_drag_and_drop_button(self):
        self.click_element(self.locator.DragAndDrop)

    def perform_drag_and_drop(self):
        self.drag_and_drop(self.locator.source_location, self.locator.destination_location)

    #https://www.globalsqa.com/demo-site/draganddrop/
    def switch_to_drag_and_drop_iframe(self):
        self.switch_to_iframe(self.locator.iframe)
