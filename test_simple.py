from unittest import TestCase
from simple import get_message_encoding

class SimpleTestCase(TestCase):
    def test_get_message_encoding(self):
        message = [("लो यह टेस्ट एसएमएस है",2),("Vinay test Gupshup",1),("😁 😲 Pawan", 2)]

        for msg in message:
            # print(msg[0],msg[1])
            res_encoding = get_message_encoding(msg[0])
            self.assertEqual(res_encoding, msg[1])


if __name__ == '__main__':
    import unittest
    unittest.main()