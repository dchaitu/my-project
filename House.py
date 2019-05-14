from Address import Address


class House(object):
    def __init__(self, street, number, zip_code, city, n_rooms, sale_price):
        # Address.__init__(self, street,number,zip_code,city)
        # self.addr = addr

        self.obj_addr = Address(street, number, zip_code, city)
        self.n_rooms = n_rooms
        self.sale_price = sale_price

    def cost_at_most(self, price):
        if int(self.sale_price) <= price:
            print("TotalCost : {}".format(self.n_rooms * self.sale_price))
            return True

        return False

    @staticmethod
    def read(self):
        street, number, zip_code, city, n_rooms, sale_price = input(" Enter Address of House: ").split()
        return self(street, number, zip_code, city, n_rooms, sale_price)



    def __eq__(self, o):


        if (self.obj_addr.street == o.obj_addr.street and
        	self.obj_addr.number == o.obj_addr.number and
        	self.obj_addr.zip_code == o.obj_addr.zip_code and
        	self.obj_addr.city == o.obj_addr.city):
            return True
        else:
            return False

    def __str__(self):

        return self.house.obj_addr.street


if __name__ == '__main__':

    # x = House("Yendada", 123, 530045, "Vizag", 2, 2000)
    x=House.read()
    price = int(input("Enter Price"))
    x.cost_at_most(price)
    print(x.obj_addr)
    y=House.read()
    # y = House("Eendada", 1223, 530045, "Vizag", 2, 2000)
    y.cost_at_most(price)
    print(y.obj_addr)
    print(x == y)
    # z = House("Yendada", 123, 530045, "Vizag", 2, 2000)
    # print(x == z)
