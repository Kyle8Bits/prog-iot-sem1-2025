# Ref.: B. Slatkin, Effective Python: 125 Specific Ways to Write Better Python, 
# 3rd ed., Addison-Wesley Professional, 2024.

from unittest import TestCase, main
from utils import to_str

class UtilsErrorTestCase(TestCase):
    def test_to_str_bad(self):
        with self.assertRaises(TypeError):
            to_str(object())

    def test_to_str_bad_encoding(self):
        with self.assertRaises(UnicodeDecodeError):
            to_str(b"\xfa\xfa")

if __name__ == "__main__":
    main()
