import time

import pytest

from page.home_page import HomePage
from test.base_test import BaseTest

from data.data import TestData as DATA


class TestCase(BaseTest):
    @pytest.mark.sanity
    def test_autocomplete(self):
        tc = HomePage(self.driver)
        tc.click_autocomplete()
        tc.enter_address(DATA.address)
        tc.enter_street_address(DATA.street_address)
        tc.enter_street_address_2(DATA.street_address_2)
        tc.enter_city(DATA.city)
        tc.enter_state(DATA.state)
        tc.enter_zip_code(DATA.zip_code)
        tc.enter_country(DATA.country)
        time.sleep(5)

    @pytest.mark.regression
    def test_buttons(self):
        tc = HomePage(self.driver)
        tc.click_buttons()
        tc.click_primary()
        tc.click_warning()
        tc.click_left()
        tc.click_one_button()
        tc.click_drop_down()
        tc.click_drop_down_link1()
        time.sleep(2)

    @pytest.mark.sanity
    def test_checkbox(self):
        tc = HomePage(self.driver)
        tc.click_checkbox()
        tc.select_checkboxes()
        time.sleep(2)
        assert tc.assert_checkboxes() == True

    @pytest.mark.regression
    def test_checkbox1(self):
        tc = HomePage(self.driver)
        tc.click_checkbox()
        tc.select_checkboxes_checkbox3()
        time.sleep(2)
        assert tc.assert_checkboxes_checkbox3() == True

    def test_date(self):
        tc = HomePage(self.driver)
        tc.click_datepicker()
        time.sleep(3)
        tc.click_date()
        time.sleep(1)
        tc.enter_date(DATA.date)
        time.sleep(2)

    def test_drop(self):
        tc = HomePage(self.driver)
        tc.click_drop_down()
        time.sleep(2)
        tc.click_down()
        time.sleep(2)
        tc.click_check_box()
        time.sleep(2)

    def test_enable(self):
        tc = HomePage(self.driver)
        tc.click_enable()
        time.sleep(1)
        tc.click_input()
        tc.enter_input(DATA.input)
        time.sleep(1)

    @pytest.mark.sanity
    def test_file(self):
        tc = HomePage(self.driver)
        tc.click_file()
        time.sleep(1)
        tc.image_upload()
        time.sleep(2)

    def test_keyboard(self):
        tc = HomePage(self.driver)
        tc.click_key()
        time.sleep(1)
        tc.click_name()
        tc.enter_name(DATA.name)
        time.sleep(1)
        tc.click_button()
        time.sleep(2)

    def test_modal(self):
        tc = HomePage(self.driver)
        tc.click_modal()
        time.sleep(1)
        tc.click_open()
        time.sleep(2)
        tc.click_close()
        time.sleep(1)

    def test_large(self):
        tc = HomePage(self.driver)
        tc.click_page()
        time.sleep(1)
        tc.click_fullname()
        tc.enter_fullname(DATA.name)
        time.sleep(1)
        tc.click_birth()
        tc.enter_birth(DATA.date)
        time.sleep(2)

    def test_radiobutton(self):
        tc = HomePage(self.driver)
        tc.click_radiobutton()
        time.sleep(2)
        tc.select_radiobutton_radiobutton1()
        time.sleep(2)
        assert tc.assert_radiobutton1_selected() == True
        time.sleep(2)

    def test_tab(self):
        tc = HomePage(self.driver)
        tc.click_switch()
        time.sleep(2)
        tc.click_tab()
        time.sleep(2)
        tc.switch_to_active_tab()
        time.sleep(2)
        tc.click_switch()
        time.sleep(2)
        tc.click_alert()
        time.sleep(2)
        tc.accept_alert()
        time.sleep(2)

    def test_web(self):
        tc = HomePage(self.driver)
        tc.click_web()
        time.sleep(2)
        tc.click_firstname()
        tc.enter_firstname(DATA.name_1)
        tc.click_lastname()
        tc.enter_lastname(DATA.name_2)
        tc.click_job()
        tc.enter_job(DATA.job)
        tc.select_web_high_school()
        tc.select_web_college()
        tc.select_web_grand()
        tc.select_web_female()
        time.sleep(2)
        tc.select_number()
        time.sleep(1)
        tc.click_date_1()
        tc.enter_date_1(DATA.date)
        time.sleep(2)
        tc.click_submit_button()

    def test_drag_and_drop(self):
        dd = HomePage(self.driver)
        dd.click_on_drag_and_drop_button()
        time.sleep(2)
        dd.perform_drag_and_drop()
        time.sleep(2)

    # https://www.globalsqa.com/demo-site/draganddrop/
    def test_drag_and_drop2(self):
        dd = HomePage(self.driver)
        time.sleep(2)
        dd.switch_to_drag_and_drop_iframe()
        time.sleep(2)
        dd.perform_drag_and_drop()
        time.sleep(2)
