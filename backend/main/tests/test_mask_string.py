from unittest import TestCase
from main.utils import mask_string


class TestMaskString(TestCase):

    def test_should_mask_entire_string(self):
        string = 'string'
        actual_string = mask_string(string=string)
        expected_string = '******'
        self.assertEqual(actual_string, expected_string)

    def test_should_mask_second_half_of_the_string(self):
        string = 'string'
        half_chars_count = int(len(string) / 2)
        actual_string = mask_string(string=string, masked_chars_count=half_chars_count)
        expected_string = 'str***'
        self.assertEqual(actual_string, expected_string)

    def test_should_mask_first_half_of_the_string(self):
        string = 'string'
        half_chars_count = int(len(string) / 2)
        actual_string = mask_string(string=string, masked_chars_count=half_chars_count, starts_from_end=False)
        expected_string = '***ing'
        self.assertEqual(actual_string, expected_string)
