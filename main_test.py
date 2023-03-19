import unittest
import main as data_agg


class MyTestCase(unittest.TestCase):
    def test_data_agg_1(self):
        """
        Test summary for data1 file
        :return:
        """
        expected_result = "Name: JOHN DOE, Id: 123, Exam Count: 0\n" \
                          "Name: JANE CROW, Id: 789, Exam Count: 2\n"
        actual_result = data_agg.process_file("data1")
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_data_agg_2(self):
        """
        Test data2 file
        :return:
        """
        expected_result = "Name: JOHN DOE, Id: 123, Exam Count: 0\n" \
                          "Name: JOE SCMOE, Id: 321, Exam Count: 0\n"
        actual_result = data_agg.process_file("data2")
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_data_agg_3(self):
        """
        Test data3 file
        :return:
        """
        expected_result = "Name: JOHN DOE, Id: 123, Exam Count: 1\n"
        actual_result = data_agg.process_file("data3")
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_data_agg_4(self):
        """
        Test data2 file
        :return:
        """
        expected_result = "Name: DOE JOHN, Id: 123, Exam Count: 0\n" \
                          "Name: JOHN DOE, Id: 124, Exam Count: 2\n"
        actual_result = data_agg.process_file("data4")
        self.assertEqual(expected_result, actual_result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
