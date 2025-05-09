# Ref.: B. Slatkin, Effective Python: 125 Specific Ways to Write Better Python, 
# 3rd ed., Addison-Wesley Professional, 2024.

from unittest import TestCase, main

def setUpModule():
    print("* Module setup")

def tearDownModule():
    print("* Module clean-up")

class IntegrationTest(TestCase):
    def setUp(self):
        print("* Test setup")

    def tearDown(self):
        print("* Test clean-up")

    def test_end_to_end1(self):
        print("* Test 1")

    def test_end_to_end2(self):
        print("* Test 2")

if __name__ == "__main__":
    main()
