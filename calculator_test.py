import unittest
from appium import webdriver


class calculator_test(unittest.TestCase):
    calcsession = None

    def setUp(self):
        print("Setup")
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.calcsession = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            desired_capabilities=desired_caps
        )

    def tearDown(self):
        print('TearDown')
        self.calcsession.quit()

    def test_add(self):
        print("Add")
        self.calcsession.find_element_by_name("One").click()
        self.calcsession.find_element_by_name("Two").click()
        self.calcsession.find_element_by_name("Plus").click()
        self.calcsession.find_element_by_name("Nine").click()
        self.calcsession.find_element_by_name("Equals").click()
        self.assertEqual(self.getDisplayResults(), "21")

    def test_Sub(self):
        print("Sub")
        self.calcsession.find_element_by_name("Two").click()
        self.calcsession.find_element_by_name("Minus").click()
        self.calcsession.find_element_by_name("Nine").click()
        self.calcsession.find_element_by_name("Equals").click()
        self.assertEqual(self.getDisplayResults(), "-7")

    def test_Mul(self):
        print("Mul")
        self.calcsession.find_element_by_name("Eight").click()
        self.calcsession.find_element_by_name("Multiply by").click()
        self.calcsession.find_element_by_name("Nine").click()
        self.calcsession.find_element_by_name("Equals").click()
        self.assertEqual(self.getDisplayResults(), "72")

    def test_Div(self):
        print("Div")
        self.calcsession.find_element_by_name("One").click()
        self.calcsession.find_element_by_name("Divide by").click()
        self.calcsession.find_element_by_name("Zero").click()
        self.calcsession.find_element_by_name("Equals").click()
        self.assertEqual(self.getDisplayResults(), "Cannot divide by zero")

    def getDisplayResults(self):
        result = self.calcsession.find_element_by_accessibility_id("CalculatorResults").text
        result = result.strip("Display is ")
        return result
