import pytest
import numpy as np
from python_matrix import matrix_

class Test_matrix:

    def test_matrix(self):
        with pytest.raises(ValueError):
            matrix_(-5)

        expected_result = np.array([[1, 2], [4, 3]])
        assert np.array_equal(matrix_(2), expected_result)

        expected_result = np.array([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
        assert np.array_equal(matrix_(3), expected_result)

        expected_result = np.array([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
        assert np.array_equal(matrix_(4), expected_result)
