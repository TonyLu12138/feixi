import pytest
import math
from python_list import compare_list

class TestCompareLists:
    def test_compare_list(self):
        input_a = ['apple', 'banana', 'orange']
        input_b = ['banana', 'kiwi', 'grape']
        expected_result = ['banana']
        assert compare_list(input_a, input_b) == expected_result

        input_a = ['apple', 'banana', 'orange']
        input_b = ['kiwi', 'grape']
        expected_result = []
        assert compare_list(input_a, input_b) == expected_result

        input_a = []
        input_b = ['kiwi', 'grape']
        expected_result = []
        assert compare_list(input_a, input_b) == expected_result

        input_a = ['apple', 'banana', 'orange']
        input_b = []
        expected_result = []
        assert compare_list(input_a, input_b) == expected_result

        input_a = []
        input_b = []
        expected_result = []
        assert compare_list(input_a, input_b) == expected_result

        input_a = ['apple', 0, 2147483647, 2.9,True,math.e]
        input_b = [0, '0', 'applee', 2147483648, True, 2.718281828459045]
        expected_result = [0, True, 2.718281828459045]
        assert compare_list(input_a, input_b) == expected_result