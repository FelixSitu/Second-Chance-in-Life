import unittest
from Practice import *
from string import *


class Practice_Test(unittest.TestCase):
    def test_triples(self):
        lst1 = [1,2,5,6,7,7,7,10,7,7,7]
        print find_triple(lst1) # returns [4,8]

    def test_get_nums(self):
        lst1 = [1, 2, 5, 6, 7, 7, 7, 10, 7, 7, 7]
        print get_nums(lst1)

    def test_get_capital(self):
        words1 = ['HEllo','Goodbye','etc.']
        print get_captials(words1)

    def test_get_col(self):
        matrix1 = [[1,0,0],[0,1,0],[0,0,1]]
        print get_columns(matrix1,2)

    def test_add_numbers(self):
        string1 = '12xyz?!9'
        print add_numbers(string1)

    def test_add_list(self):
        list1 = [1,2,3]
        list2 = [4,5,6]
        print add_list_idx(list1,list2)

    def test_idx_small(self):
        list1 = [9,7,7,4,3]
        print index_of_smallest(list1)

if __name__ == "__main__":
    unittest.main()