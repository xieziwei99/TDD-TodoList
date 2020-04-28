from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):     # 测试类以Test结尾
    def setUp(self):    # 在所有test之前运行
        # return super().setUp()
        self.browser = webdriver.Firefox()

    def tearDown(self):     # 在所有test之后运行
        # return super().tearDown()
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):      # 测试方法以test开头
        # 张三进入网站首页
        self.browser.get(self.live_server_url)

        # 张三注意到页的title是To-Do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 他被邀请去做一个to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute(
            'placeholder'), 'Enter a to-do item')

        # 张三在文本框中输入"Buy peacock features"
        inputbox.send_keys('Buy peacock features')

        # 他按下enter，页面更新了，在to-do lists中显示出"1: Buy peacock features"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # # self.assertTrue(any(row.text == '1: Buy peacock features' for row in rows),
        # #                 f"New to-do item did not appear in table. Contents were:\n{table.text}")
        # self.assertIn('1: Buy peacock features', [row.text for row in rows])
        self.check_for_row_in_list_table('1: Buy peacock features')

        # 这里还有一个输入框让他输入另外一个项，他输入"Use peacock features to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock features to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # 页面又更新了，显示出两条item
        self.check_for_row_in_list_table('1: Buy peacock features')
        self.check_for_row_in_list_table(
            '2: Use peacock features to make a fly')

        # 张三想知道网站是否记住了他的代办列表，他发现网站为他生成了一个独立的URL

        # 他再次访问了那个URL，发现to-do list还在

        # 他很满意的睡觉去了

        self.fail('Finish the test.')

    def check_for_row_in_list_table(self, row_text: str):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])