import pytest

from ..src.puzzle import Puzzle

def test_index():
    puzzle = Puzzle()

    puzzle.board[0][0] = 8

    assert puzzle.index(0,0) == 8

def test_set_value():
    puzzle = Puzzle()

    puzzle.set_value(0,0,8)

    assert puzzle.board[0][0] == 8
    
def test_validate_list():

    puzzle = Puzzle()

    l1 = [1,2,3,4]
    l2 = [1,1,2,3]
    l3 = [1]
    l4 = []

    assert puzzle._validate_list(l1)
    assert not puzzle._validate_list(l2)
    assert puzzle._validate_list(l1)
    assert puzzle._validate_list(l1)


def test_get_next_index():
    puzzle = Puzzle()
    x1, y1 = puzzle.get_next_index(0,0)
    assert x1 == 0 and y1 == 0

    puzzle.board[3][3] == 1
    x2, y2 = puzzle.get_next_index(2,3)
    assert x2 == 2 and y2 == 3

    puzzle.board[8][8] = 1
    x3, y3 = puzzle.get_next_index(8,8)
    assert x3 == -1 and y3 == -1

    puzzle.board[0][0] = 1
    x4, y4 = puzzle.get_next_index(0,0)
    assert x4 == 1 and y4 == 0
    