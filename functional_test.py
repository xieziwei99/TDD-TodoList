from selenium import webdriver
import unittest

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
        self.fail('Finish the test.')

if __name__ == "__main__":
    unittest.main()

# 他被邀请去做一个to-do item

# 张三在文本框中输入"Buy peacock features"

# 他按下enter，页面更新了，在to-do lists中显示出"1: Buy peacock features"

# 这里还有一个输入框让他输入另外一个项，他输入"Use peacock features to make a fly"

# 页面又更新了，显示出两条item

# 张三想知道网站是否记住了他的代办列表，他发现网站为他生成了一个独立的URL

# 他再次访问了那个URL，发现to-do list还在

# 他很满意的睡觉去了