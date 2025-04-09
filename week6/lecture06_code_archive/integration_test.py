# Ref.: B. Slatkin, Effective Python: 125 Specific Ways to Write Better Python, 
# 3rd ed., Addison-Wesley Professional, 2024.

from unittest import TestCase, main
from integration import Toaster, ReusableTimer

class ToasterIntegrationTest(TestCase):

    def setUp(self):
        self.timer = ReusableTimer()
        self.toaster = Toaster(self.timer)
        self.toaster.level = 0

    def test_wait_finish(self):
        self.assertFalse(self.toaster.hot)
        self.toaster.push_down()
        self.assertTrue(self.toaster.hot)
        self.timer.timer.join()
        self.assertFalse(self.toaster.hot)

    def test_cancel_early(self):
        self.assertFalse(self.toaster.hot)
        self.toaster.push_down()
        self.assertTrue(self.toaster.hot)
        self.toaster.pop_up()
        self.assertFalse(self.toaster.hot)

if __name__ == "__main__":
    main()
