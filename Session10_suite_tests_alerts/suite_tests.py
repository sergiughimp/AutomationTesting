import unittest

from Session9_waits.test_unit import FirstTestCase, JulesTestCases
from Session9_waits.homework_session9 import Login
from Session10_suite_tests_alerts.alerts import AlertsTests
import HtmlTestRunner
class TestSuite(unittest.TestCase):
    def test_suite(self):
        # object from TestSuite class
        my_test_suite = unittest.TestSuite()
        # list with all the test from the classes
        my_test_suite.addTests([
            # unittest.defaultTestLoader.loadTestsFromTestCase(FirstTestCase),
            # unittest.defaultTestLoader.loadTestsFromTestCase(JulesTestCases),
            # unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(AlertsTests)
        ])

        # create an HTML runner, that will generate reports for all the test
        test_runner = HtmlTestRunner.HTMLTestRunner(
            report_title="Test Cases Report",
            report_name="Jules",
            combine_reports=True
        )
        # run all the test suite
        test_runner.run(my_test_suite)