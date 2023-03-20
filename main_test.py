import unittest
import main as data_agg


class MyTestCase(unittest.TestCase):
    def test_data_agg_1(self):
        """
        Test summary for data1 file
        tests deleting a patient, adding a patient and adding exams
        edge cased tested : attempting to add a patient with an id that is already
            occupied by a different patient
        :return:
        """
        expected_result = "Name: JOHN DOE, Id: 123, Exam Count: 0\n" \
                          "Name: JANE CROW, Id: 789, Exam Count: 2\n"
        actual_result = data_agg.process_file("data1")
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_data_agg_2(self):
        """
        Test data2 file
        tests adding two different patients with their own unique id
        :return:
        """
        expected_result = "Name: JOHN DOE, Id: 123, Exam Count: 0\n" \
                          "Name: JOE SCMOE, Id: 321, Exam Count: 0\n"
        actual_result = data_agg.process_file("data2")
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_data_agg_3(self):
        """
        Test data3 file
        tests adding an exam to a patient
        edge cases tested :
            -attempting to add an exam that has a patient id that does not exist
            -attempting to add an exam that has an exam id that already exists
        :return:
        """
        expected_result = "Name: JOHN DOE, Id: 123, Exam Count: 1\n"
        actual_result = data_agg.process_file("data3")
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_data_agg_4(self):
        """
        Test data4 file
        tests adding a patient and exam as well as deleting an exam
        edge case tested : attempting to delete an exam that contains an exam id that
            does not exist
        :return:
        """
        expected_result = "Name: DOE JOHN, Id: 123, Exam Count: 0\n" \
                          "Name: JOHN DOE, Id: 124, Exam Count: 2\n"
        actual_result = data_agg.process_file("data4")
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_data_agg_5(self):
        """
        Test data5 file
        attempts adding and deleting a patient as well as the summary when the patient
        record is empty
        edge case tested: attempting to delete a patient with a non existing patient id
        :return:
        """
        expected_result = ""
        actual_result = data_agg.process_file("data5")
        self.assertEqual(expected_result, actual_result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
