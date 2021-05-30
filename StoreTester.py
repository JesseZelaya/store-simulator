# Author: Jesse Zelaya
# Date: 6/24/2020
# Description: Unit test script tests different values to assure proper results are calculated

import Store
import unittest


class TestStoreCases(unittest.TestCase):
    """
    Test list for store program 162 project 2
    """

    def test_1(self):
        #check id of product
        p1 = Store.Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p1_id = p1.get_product_id()
        self.assertEqual(p1_id, "889", "id incorrect")

    def test_2(self):
        # check quantity available
        p1 = Store.Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p1_quantity = p1.get_quantity_available()
        self.assertEqual(p1_quantity, 8, "incorrect quantity")

    def test_3(self):
        """check if premium member for valid member"""
        c1 = Store.Customer("harold", "qcf", True)
        self.assertTrue(c1.is_premium_member(), "not premium member")

    def test_4(self):
        """check if premium member if not valid"""
        c1 = Store.Customer("harold", "qcf", False)
        self.assertFalse(c1.is_premium_member(), "IS premium member")

    def test_5(self):
        # test store object methods
        p1 = Store.Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        myStore = Store.Store()
        myStore.add_product(p1)
        self.assertIs(myStore.get_product_from_id("889"), p1, "not the same product object")

    def test_6(self):
        """test check out should equal 6.42 for three items at 2 dollars each plus shipping"""
        toothpaste = Store.Product(11, "toothpaste", "dental", 2, 4)
        milk = Store.Product(12, "milk", "dairy", 2, 3)
        eggs = Store.Product(14, "eggs", "dairy", 2, 2)
        apple_juice = Store.Product(13, "apple juice", "drink", 1, 1)

        s = Store.Store()
        s.add_product(toothpaste)
        s.add_product(milk)
        s.add_product(eggs)
        s.add_product(apple_juice)

        henry = Store.Customer("henry", "mrh", False)
        s.add_member(henry)

        s.add_product_to_member_cart(11, "mrh")
        s.add_product_to_member_cart(12, "mrh")
        s.add_product_to_member_cart(14, "mrh")
        self.assertAlmostEqual(s.check_out_member("mrh"), 6.42, "not the correct checkout amount")

if __name__ == '__main__':
    unittest.main()
