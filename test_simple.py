

import unittest

from .__main__ import PythonVnfm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        vnfm = PythonVnfm()
        self.assertIsNotNone(vnfm)


if __name__ == '__main__':
    unittest.main()
