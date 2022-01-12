"""
Assignment 2: Quadtree Compression

=== CSC148 Winter 2021 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains the test suite
"""

import pytest
from a2tree import QuadTreeNode, QuadTreeNodeEmpty, QuadTreeNodeLeaf, QuadTree

"""
Test cases
"""


def test_split_quadrants_1():
    tree = QuadTree()
    split = tree._split_quadrants([[8, 9], [3, 4]])
    assert split == [[[8]], [[9]], [[3]], [[4]]]


def test_split_quadrants_2():
    tree = QuadTree()
    split = tree._split_quadrants([[2, 4, 1], [6, 8, 10]])
    assert split == [[[2]], [[4, 1]], [[6]], [[8, 10]]]


def test_split_quadrants_3():
    tree = QuadTree()
    split = tree._split_quadrants([[1, 2, 3, 4, 5, 6]])
    assert split == [[], [], [[1, 2, 3]], [[4, 5, 6]]]


def test_restore_from_preorder_1():
    tree = QuadTree()
    tree.build_quad_tree([[11, 2, 23], [2, 5, 9], [3, 1, 7], [10, 1, 1]])
    lst = tree.preorder().split(",")
    new_tree = tree.restore_from_preorder(lst, 3, 4)
    new_lst = new_tree.preorder().split(",")
    assert lst == new_lst
    pass


def test_restore_from_preorder_2():
    tree = QuadTree()
    tree.build_quad_tree([[2, 17], [13, 24]])
    lst = tree.preorder().split(",")
    new_tree = tree.restore_from_preorder(lst, 2, 2)
    new_lst = new_tree.preorder().split(",")
    assert lst == new_lst
    pass


def test_restore_from_preorder_3():
    tree = QuadTree()
    tree.build_quad_tree([[10], [9], [8], [7]])
    lst = tree.preorder().split(",")
    new_tree = tree.restore_from_preorder(lst, 1, 4)
    new_lst = new_tree.preorder().split(",")
    assert lst == new_lst
    pass


if __name__ == '__main__':
    pytest.main(['a2test_student.py'])
