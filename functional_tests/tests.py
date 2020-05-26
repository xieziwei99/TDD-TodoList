from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 2


# LiveServerTestCase 会自动创建一个测试数据库 并启动一个开发服务器来运行功能测试
# 因此，可以直接使用 python manage.py test .\functional_tests\ 来运行测试，而不需要提前运行 runserver


class NewVisitorTest(LiveServerTestCase):  # 测试类以Test结尾
    def setUp(self):  # 在所有test之前运行
        # return super().setUp()
        self.browser = webdriver.Firefox()

    def tearDown(self):  # 在所有test之后运行
        # return super().tearDown()
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  # 测试方法以test开头
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

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # # self.assertTrue(any(row.text == '1: Buy peacock features' for row in rows),
        # #                 f"New to-do item did not appear in table. Contents were:\n{table.text}")
        # self.assertIn('1: Buy peacock features', [row.text for row in rows])
        self.wait_for_row_in_list_table('1: Buy peacock features')

        # 这里还有一个输入框让他输入另外一个项，他输入"Use peacock features to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock features to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # 页面又更新了，显示出两条item
        self.wait_for_row_in_list_table('1: Buy peacock features')
        self.wait_for_row_in_list_table(
            '2: Use peacock features to make a fly')

        # 他再次访问了那个URL，发现to-do list还在

        # 他很满意的睡觉去了

    def wait_for_row_in_list_table(self, row_text: str):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Buy peacock features")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock features")

        # 张三想知道网站是否记住了他的代办列表，他发现网站为他生成了一个独立的URL
        zhangsan_list_url = self.browser.current_url
        self.assertRegex(zhangsan_list_url, '/lists/.+')  # .+ 贪婪匹配

        # 一个新用户李四来到的网站
        # 我们使用一个新的 session 来确保 cookies 中不含有张三的信息
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # 李四访问主页，发现没有张三的 lists
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock features', page_text)
        self.assertNotIn('make a fly', page_text)

        # 李四输入了一个新的 item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # 李四得到了他的唯一的 url
        lisi_list_url = self.browser.current_url
        self.assertRegex(lisi_list_url, '/lists/.+')
        self.assertNotEqual(lisi_list_url, zhangsan_list_url)

        # 再次检查没有张三的 lists
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock features', page_text)
        self.assertIn('Buy milk', page_text)

        # 张三和李四都满意的睡觉去了

    def test_layout_and_styling(self):
        # 张三来到主页
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # 他注意到输入框放到中间了
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=10)

        # 他新启了一个 list，注意到输入框也放在中间
        inputbox.send_keys("testing")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2, 512, delta=10)
