import unittest
from unittest.mock import patch
from main import magic_square
from main import check_blood_pressure
import re


def normalize_string(s):
    # Lowercase, remove all non-alphanumeric characters (except spaces), then remove extra spaces
    return re.sub(r'\s+', ' ', re.sub(r'[^a-z0-9\s]', '', s.lower())).strip()

def normalize_multiline(s):
    return [line.strip() for line in s.strip().split('\n')]

class TestAssessment(unittest.TestCase):

    # Test for normal blood pressure
    @patch('builtins.input', side_effect=[119, 79])
    def test_normal(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Normal"), normalize_string(result))

    # Test for elevated blood pressure
    @patch('builtins.input', side_effect=[125, 79])
    def test_elevated(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Elevated"), normalize_string(result))

    # Test for Stage 1 Hypertension - 1
    @patch('builtins.input', side_effect=[135, 79])
    def test_stage_1_hypertension1(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Stage 1 Hypertension"), normalize_string(result))

    # Test for Stage 1 Hypertension - 2
    @patch('builtins.input', side_effect=[125, 80])
    def test_stage_1_hypertension2(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Stage 1 Hypertension"), normalize_string(result))

    # Test for Stage 1 Hypertension - 3
    @patch('builtins.input', side_effect=[130, 89])
    def test_stage_1_hypertension3(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Stage 1 Hypertension"), normalize_string(result))

    # Test for Stage 2 Hypertension - 1
    @patch('builtins.input', side_effect=[140, 89])
    def test_stage_2_hypertension1(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Stage 2 Hypertension"), normalize_string(result))

    # Test for Stage 2 Hypertension - 2
    @patch('builtins.input', side_effect=[139, 90])
    def test_stage_2_hypertension2(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Stage 2 Hypertension"), normalize_string(result))

    # Test for Stage 2 Hypertension - 3
    @patch('builtins.input', side_effect=[141, 102])
    def test_stage_2_hypertension3(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Stage 2 Hypertension"), normalize_string(result))

    # Test for Hypertensive Crisis - 1
    @patch('builtins.input', side_effect=[185, 130])
    def test_hypertensive_crisis1(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Hypertensive Crisis - Immediate medical attention needed"), normalize_string(result))

    # Test for Hypertensive Crisis - 2
    @patch('builtins.input', side_effect=[185, 80])
    def test_hypertensive_crisis2(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Hypertensive Crisis - Immediate medical attention needed"), normalize_string(result))

    # Test for invalid input
    @patch('builtins.input', side_effect=[-1, 80])
    def test_invalid_systolic_input1(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Invalid input"),
                         normalize_string(result))

    # Test for invalid input
    @patch('builtins.input', side_effect=[120, -80])
    def test_invalid_systolic_input2(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Invalid input"),
                         normalize_string(result))

    # Test for invalid input
    @patch('builtins.input', side_effect=[-1, -80])
    def test_invalid_systolic_input3(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Invalid input"),
                         normalize_string(result))

    # Test for Hypertensive Crisis - 3
    @patch('builtins.input', side_effect=[140, 121])
    def test_hypertensive_crisis3(self, mock_input):
        result = check_blood_pressure()
        self.assertEqual(normalize_string("Hypertensive Crisis - Immediate medical attention needed"), normalize_string(result))




    def test_invalid_symbol(self):
        self.assertEqual(magic_square(2, '!'), "Invalid symbol")

    def test_invalid_number(self):
        self.assertEqual(magic_square(-2, 'B'), "Invalid number")

    def test_invalid_symbol_and_invalid_number(self):
        self.assertEqual(magic_square(-2, '!'), "Invalid number and invalid symbol")

    def test_start_A_size_4(self):
        expected = """A B C D
        E F G H
        I J K L
        M N O P """

        self.assertEqual(normalize_multiline(magic_square(4, 'A')),
                         normalize_multiline(expected))

    def test_start_X_size_4(self):
        expected = """X Y Z A 
                    B C D E 
                    F G H I 
                    J K L M"""

        # Normalize by stripping spaces from each line
        self.assertEqual(normalize_multiline(magic_square(4, 'X')),
                         normalize_multiline(expected))

    def test_start_K_size_6(self):
        expected = """
        K L M N O P 
        Q R S T U V 
        W X Y Z A B 
        C D E F G H 
        I J K L M N 
        O P Q R S T """

        # Normalize by stripping spaces from each line
        self.assertEqual(normalize_multiline(magic_square(6, 'K')),
                         normalize_multiline(expected))
