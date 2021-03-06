""" This module contains code for the tests for the trie
class """
import unittest
from py.data_structures.trie import Trie


class TrieTests(unittest.TestCase):
    """ This class contains tests for the trie data structure """

    def test1(self):
        obj1 = Trie()
        obj1.insert("Cat")
        obj1.insert("cat")

        self.assertEqual(True, obj1.lookup("Cat"))
        self.assertEqual(True, obj1.lookup("cat"))
        self.assertEqual(False, obj1.lookup("ca"))
        self.assertEqual(False, obj1.lookup("c"))

        self.assertEqual(True, obj1.starts_with("ca"))
        self.assertEqual(True, obj1.starts_with("C"))

    def test2(self):
        obj1 = Trie()
        obj1.insert("cat")
        obj1.insert("call")

        obj1.delete("cat")

        # deleting cat should leave call in
        self.assertEqual(False, obj1.lookup("cat"))
        self.assertEqual(True, obj1.lookup("call"))

        obj1.insert("back")
        obj1.insert("backly")
        obj1.insert("backl")

        obj1.delete("backl")
        self.assertEqual(False, obj1.lookup("backl"))
        self.assertEqual(True, obj1.lookup("backly"))
        self.assertEqual(True, obj1.lookup("back"))


if __name__ == "__main__":
    unittest.main()
