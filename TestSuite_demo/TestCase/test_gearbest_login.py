import unittest
from Public.Decorator import *
from Public.Test_data import get_test_data
from PageObject import GbLoginPage


class TestGbLogin(unittest.TestCase, BasePage):
    @classmethod
    @setupclass
    def setUpClass(cls):
        cls.d.app_start("com.globalegrow.app.gearbest")  # restart app
        cls.test_data = get_test_data(cls.d)

    @classmethod
    @teardownclass
    def tearDownClass(cls):
        cls.d.app_stop("com.globalegrow.app.gearbest")  # restart app

    @testcase
    def test_login(self):
        loginPage = GbLoginPage.GbLoginPage()
        loginPage.wait_page()
        self.set_fastinput_ime()
        loginPage.login(self.test_data['user_name'], self.test_data['password'])
        print('登录成功')
