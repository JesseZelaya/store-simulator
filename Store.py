# Author: Jesse Zelaya
# Date: 6/24/2020
# Description: Group of classes that represent products, customers and
#              store fronts. Using them together, the user can simulate
#              a storefront.


class Product:
    def __init__(self, ID, title, description, price, quantity_available):
        """initializes parameters related to Product class"""
        self._ID = ID
        self._title = title
        self._description = description
        self._price = price
        self._quantity_available = quantity_available

    def get_product_id(self):
        """gets product id and returns it"""
        return self._ID

    def get_title(self):
        """gets title of product"""
        return self._title

    def get_description(self):
        """get description of product"""
        return self._description

    def get_price(self):
        """get price of product"""
        return self._price

    def get_quantity_available(self):
        """get the quantity of the product"""
        return self._quantity_available

    def decrease_quantity(self):
        """decreases quantity of availability by one"""
        try:
            one_less = self._quantity_available - 1
            if one_less < 0:
                raise ValueError()
        except ValueError:
            print("Error: Quantity already at zero.")
        else:
            self._quantity_available -= 1


class Customer:
    """represents customer with name and account ID"""

    def __init__(self, name, ID, premium_member):
        self._name = name
        self._ID = ID
        self._premium_member = premium_member
        self._customer_cart = []

    def get_name(self):
        """gets customer name"""
        return self._name

    def get_customer_id(self):
        """gets customer id"""
        return self._ID

    def is_premium_member(self):
        """returns true or false if customer is premium member"""
        return self._premium_member

    def add_product_to_cart(self, product_id):
        """takes product ID and adds it to customer's cart"""
        self._customer_cart.append(product_id)

    def get_customer_cart(self):
        """returns list of customer object cart contents"""
        return self._customer_cart

    def empty_cart(self):
        """emties customer cart"""
        self._customer_cart = []


class DuplicateObject(Exception):
    """exception to raise when attempted duplicate item added to inventory"""
    pass


class InvalidCheckoutError(Exception):
    """exception to raise when invalid customer id is given"""
    pass

class Store:
    """represent a store which has some number of products in its
       inventory and some number of customer members"""

    def __init__(self):
        self._inventory = {}
        self._membership = {}

    def add_product(self, product):
        """adds product to the store inventory without duplicate id"""
        try:
            if product.get_product_id() in self._inventory:
                raise DuplicateObject()
        except DuplicateObject:
            print("error: duplicate item in inventory")
        else:
            self._inventory[product.get_product_id()] = product

    def add_member(self, customer):
        """adds customer to store """
        try:
            if customer.get_customer_id() in self._membership:
                raise DuplicateObject()
        except DuplicateObject:
            print("error: member already exists")
        else:
            self._membership[customer.get_customer_id()] = customer

    def get_product_from_id(self, product_id):
        """returns product object if id is correct
           returns none if no product object
           using exception handling"""
        try:
            self._inventory[product_id]
        except KeyError:
            return None
        else:
            product = self._inventory[product_id]
            return product

    def get_member_from_id(self, member_id):
        """returns the member object related to the
           id given. If the id is not valid it returns
           none by exception handling"""
        try:
            self._membership[member_id]
        except KeyError:
            return None
        else:
            customer = self._membership[member_id]
            return customer

    def product_search(self, search_term):
        """returns list of lexicographic order
           product IDs that contain the search
           term in its name or description"""
        search_li = []
        if len(self._inventory) > 0:
            for val in self._inventory:
                product = self._inventory[val]
                if search_term.lower() in product.get_title().lower() or search_term in product.get_description().lower():
                    product_num = product.get_product_id()
                    #if product_num not in search_li:
                    search_li.append(product_num)
        search_li = sorted(search_li)
        return search_li

    def add_product_to_member_cart(self, product_id, member_id):
        """adds product to member cart"""
        try:
            self._inventory[product_id]
        except KeyError:
            return "product ID not found."
        else:
            try:
                self._membership[member_id]
            except KeyError:
                return "member ID not found"
            else:
                if (self._inventory[product_id].get_quantity_available()) < 1:
                    return "product out of stock"
                else:
                    customer = self._membership[member_id]
                    #print(customer.get_customer_cart(), "before add")
                    customer.add_product_to_cart(product_id)
                    #print(customer.get_customer_cart(), "after add")

                    return "product added to cart"
                # print(hello)
                # return hello

    def check_out_member(self, customer_id):
        """totals out customer cart and adds shipping costs"""
        try:
            if self.get_member_from_id(customer_id) is None:
                raise InvalidCheckoutError()
        except InvalidCheckoutError:
            print("no member id")
        else:
            #print("valid id")
            customer = self.get_member_from_id(customer_id)
            cart = customer.get_customer_cart()
            total_cost = 0
            for num in cart:
                product = self._inventory[num]
                if product.get_quantity_available() > 0:
                    total_cost += product.get_price()
                    #print(product.get_quantity_available(), "after")
                    product.decrease_quantity()
                    #print(product.get_quantity_available(), "after")
                    #print(total_cost)

            if customer.is_premium_member():
                pass
            elif customer.is_premium_member() is False:
                total_cost = total_cost * 1.07
                #print(total_cost)
            customer.empty_cart()
            return total_cost


if __name__ == '__main__':
    p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
    c1 = Customer("Yinsheng", "QWF", True)
    myStore = Store()
    myStore.add_product(p1)
    myStore.add_member(c1)
    myStore.add_product_to_member_cart("889", "QWF")
    result = myStore.check_out_member("QWF")

    toothpaste = Product(11, "toothpaste", "dental", 2, 4)
    milk = Product(12, "milk", "dairy", 2, 3)
    eggs = Product(14, "eggs", "dairy", 2, 2)
    apple_juice = Product(13, "apple juice", "drink", 1,1)

    s = Store()
    s.add_product(toothpaste)
    s.add_product(milk)
    s.add_product(eggs)
    s.add_product(apple_juice)

    henry = Customer("henry", "mrh", False)
    s.add_member(henry)

    s.add_product_to_member_cart(11, "mrh")
    s.add_product_to_member_cart(12, "mrh")
    s.add_product_to_member_cart(14, "mrh")
    s.check_out_member("mrh")
