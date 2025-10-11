import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_single_long_streak():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_multiple_streaks_longest_wins():
    # Two streaks: [2,3] length 2 and [5,6,7] length 3 -> longest is 3
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_zeros_and_negatives_break_streaks():
    assert longest_positive_streak([0, -2, 1, 2, 0, 3]) == 2

def test_all_non_positive():
    assert longest_positive_streak([0, -1, -2, 0]) == 0
