from ex3 import *


def test_sequence_monotonicity():
    assert sequence_monotonicity([1, 2, 3, 4, 5, 6, 7, 8]) == [True, True, False, False]
    assert sequence_monotonicity([1, 2, 2, 3]) == [True, False, False, False]
    assert sequence_monotonicity([7.5, 4, 3.141, 0.111]) == [False, False, True, True]
    assert sequence_monotonicity([7.5, 4, 4, 0.111]) == [False, False, True, False]
    assert sequence_monotonicity([1, 0, -1, 1]) == [False, False, False, False]
    assert sequence_monotonicity([1]) == [True, True, True, True]
    assert sequence_monotonicity([7.5, 4, 9, 9]) == [False, False, False, False]


def test_monotonicity_inverse():
    assert monotonicity_inverse(sequence_monotonicity([3, 5.55, 20, 100])) == [3, 5.55, 20, 100]
    assert monotonicity_inverse(sequence_monotonicity([5.55, 5.55, 20, 100])) == [5.55, 5.55, 20, 100]
    assert monotonicity_inverse(sequence_monotonicity([20, 20, 20, 20])) == [20, 20, 20, 20]
    assert monotonicity_inverse(sequence_monotonicity([100, 20, 5.55, 3])) == [100, 20, 5.55, 3]
    assert monotonicity_inverse(sequence_monotonicity([100, 20, 5.55, 5.55])) == [100, 20, 5.55, 5.55]
    assert monotonicity_inverse(sequence_monotonicity([5.55, 3, 100, 20])) == [5.55, 3, 100, 20]


def test_sum_of_vectors():
    assert sum_of_vectors([[1, 1], [1, 3]]) == [2, 4]
    assert sum_of_vectors([[1, 1, 1], [1, 0, 0], [0, 0, 100]]) == [2, 1, 101]
    assert sum_of_vectors([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == [2, 2, 2, 2, 2]
    assert sum_of_vectors([]) is None
    assert sum_of_vectors([[], []]) == []


def test_num_of_orthogonal():
    assert num_of_orthogonal([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    assert num_of_orthogonal([[0, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    assert num_of_orthogonal([[0, 0], [1, 2], [10, 5]]) == 2
    assert num_of_orthogonal([[1, 1, 1, 1], [2, 1, 3, 3], [0, 0, 100, 33], [8, 8, 8, 1.5], [9, 9, 9, 9]]) == 0
