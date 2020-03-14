import unittest
import onionservices

class TestOnionServices(unittest.TestCase):

    def test_get_host_name(self):
        o = onionservices.OnionServices({80: 3000})
        self.assertEqual(o.is_running(), True)

if __name__ == '__main__':
    unittest.main()
