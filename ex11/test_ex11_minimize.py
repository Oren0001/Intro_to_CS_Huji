##########################################################
#   Tester for ex11 bonus question - minimize method    #
########################################################
# Run with pytest.                                    #
# Notice that the "hard" test are not too hard.      #
#    Roy 'HaPatish' Urbach                          #
####################################################

from ex11 import Node, Diagnoser

# Here you can see the trees you test.
# Notice that hard empties are the same as easy.

emp_root = Node(None)
#  None

basic_root1 = Node('a', Node('b'), Node('b'))
#      a
#    /   \
#   b     b

basic_root2 = Node('a', Node('b', Node('c'), Node('c')), Node('d'))
#        a
#      /   \
#     b      d
#   /  \
# c     c

basic_root3 = Node('a', Node(None), Node(None))
#       a
#      / \
#   None  None

basic_empty_root = Node('a', Node('b'), Node('c', Node(None), Node('d')))
#        a
#      /   \
#     b      d
#   /  \
# c     None

root1 = Node('a', Node('b', Node('d', Node('e'), Node(None)), Node('d', Node('e'), Node(None))), Node('c', Node(None), Node(None)))
#               a
#           /      \
#         b         c
#      /    \     /   \
#    d       d  None  None
#   /\      / \
#  e  None e  None

root1_emp = Node('a', Node('b', Node('d', Node('e'), Node(None)), Node('d', Node('e'), Node(None))), Node('c', Node(None), Node(None)))
#               a
#           /      \
#         b         c
#      /    \     /   \
#    d       d  None  None
#   /\      / \
#  e  None e  None

root2 = Node('a', Node('b', Node('c', Node(None), Node('e', Node(None), Node(None))), Node('d')), Node('b', Node(None), Node('d')))
#               a
#           /      \
#         b          b
#      /    \      /   \
#     c       d   None  d
#   /   \
# None   e
#      /  \
#    None  None

root2_emp = Node('a', Node('b', Node('c', Node(None), Node('e', Node(None), Node(None))), Node('d')), Node('b', Node(None), Node('d')))
#               a
#           /      \
#         b          b
#      /    \      /   \
#     c       d   None  d
#   /   \
# None   e
#      /  \
#    None  None


# Tests:

def test_sanity():
    emp_diag = Diagnoser(emp_root)
    emp_diag.minimize()
    emp_root_lst = []
    lst_a_tree(emp_root, emp_root_lst)
    assert emp_root_lst == [None]


def test_without_empty_easy():
    basic_diagnose1 = Diagnoser(basic_root1)
    basic_diagnose1.minimize()
    basic_root1_lst = []
    lst_a_tree(basic_root1, basic_root1_lst)
    basic_diagnose2 = Diagnoser(basic_root2)
    basic_diagnose2.minimize()
    basic_root2_lst = []
    lst_a_tree(basic_root2, basic_root2_lst)
    basic_diagnose3 = Diagnoser(basic_root3)
    basic_diagnose3.minimize()
    basic_root3_lst = []
    lst_a_tree(basic_root3, basic_root3_lst)

    assert basic_root1_lst == ['b']
    assert basic_root2_lst == ['c', 'a', 'd']
    assert basic_root3_lst == [None]


def test_without_empty_harder():
    diagnose1 = Diagnoser(root1)
    diagnose1.minimize()
    root1_lst = []
    lst_a_tree(root1, root1_lst)
    diagnose2 = Diagnoser(root2)
    diagnose2.minimize()
    root2_lst = []
    lst_a_tree(root2, root2_lst)

    assert root1_lst == ['e', 'd', None, 'a', None]
    assert root2_lst == [None, 'b', 'd']


def test_empty_sanity():
    emp_diag = Diagnoser(emp_root)
    emp_diag.minimize(True)
    emp_root_lst = []
    lst_a_tree(emp_root, emp_root_lst)

    assert emp_root_lst == [None]


def test_empty_easy():
    diag_easy_emp = Diagnoser(basic_empty_root)
    diag_easy_emp.minimize(True)
    easy_empty_root_lst = []
    lst_a_tree(basic_empty_root, easy_empty_root_lst)
    assert easy_empty_root_lst == ['b', 'a', 'd']


def test_empty_harder():
    diagnose1_1 = Diagnoser(root1_emp)
    diagnose1_1.minimize(True)
    root1_1_lst = []
    lst_a_tree(root1_emp, root1_1_lst)
    diagnose2_1 = Diagnoser(root2_emp)
    diagnose2_1.minimize(True)
    root2_1_lst = []
    lst_a_tree(root2_emp, root2_1_lst)

    assert root1_1_lst == ['e']
    assert root2_1_lst == ['d']


def lst_a_tree(tree_node, lst):
    """not a test, just a function to help the tests"""
    if tree_node.positive_child is not None:
        lst_a_tree(tree_node.positive_child, lst)
    lst.append(tree_node.data)
    if tree_node.negative_child is not None:
        lst_a_tree(tree_node.negative_child, lst)
