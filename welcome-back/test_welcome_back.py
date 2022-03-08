import unittest
from main import restore_user, save_user
import json


class WelcomeBackTestCase(unittest.TestCase):
    """测试 welcome back 方法"""

    def setUp(self):
        self.filename = 'user.json'

    def test_save_user(self):
        """测试存储用户名到 json 文件"""

        save_user('xfy')
        with open(self.filename, 'r') as f:
            users = json.load(f)
            self.assertTrue('xfy' in users)

    def test_restore_user(self):
        """测试从 json 文件中恢复用户名"""

        users = restore_user()
        self.assertTrue('xfy' in users)


if __name__ == '__main__':
    unittest.main()
