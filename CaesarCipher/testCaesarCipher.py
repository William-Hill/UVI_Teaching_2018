import unittest
import logging
import WakandaCaesarCipher

logger = logging.getLogger(__name__)

class test_Caesar_cipher(unittest.TestCase):

    def test_encrypt(self):
        output = WakandaCaesarCipher.encrypt("I am King Killmonger")
        self.assertEqual(output, "M eq Omrk Omppqsrkiv")

    def test_decrypt(self):
        output = WakandaCaesarCipher.decrypt("M eq Omrk Omppqsrkiv")
        self.assertEqual(output, "I am King Killmonger")

if __name__ == '__main__':
    unittest.main(verbosity=2)
