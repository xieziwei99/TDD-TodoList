from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(unittest.TestCase):     # 测试类以Test结尾
    def setUp(self):    # 在所有test之前运行
        # return super().setUp()
        self.browser = webdriver.Firefox()

    def tearDown(self):     # 在所有test之后运行
        # return super().tearDown()
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):      # 测试方法以test开头
        # 张三进入网站首页
        self.browser.get("http://localhost:8000")

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock features' for row in rows),
                        "New to-do item did not appear in table")

        # 这里还有一个输入框让他输入另外一个项，他输入"Use peacock features to make a fly"
        self.fail('Finish the test.')


if __name__ == "__main__":
    unittest.main()


# 页面又更新了，显示出两条item

# 张三想知道网站是否记住了他的代办列表，他发现网站为他生成了一个独立的URL

# 他再次访问了那个URL，发现to-do list还在

# 他很满意的睡觉去了
