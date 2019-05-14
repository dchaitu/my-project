from Address import Address
from House import House


class HouseCatalog():

    def __init__(self,street,number,zip_code,city, n_rooms,sale_price):
        self.house = House(street,number,zip_code,city, n_rooms,sale_price)


    def add_house(self):

        l.append(self)
        print("{} Added".format(self.house.obj_addr.city))


    def houses_cost_atmost(self,price):

        if(int(self.house.sale_price)<=price):
            m.append(self.house)

    def __str__(self):

        return self.house.obj_addr.city


if __name__ == '__main__':

    l=[]
    m=[]

    price = int(input("Enter Price to Filter : "))
    x = HouseCatalog("Yendada" ,123 ,530045, "Vizag", 2, 2000)
    x.add_house()
    x.houses_cost_atmost(price)

    y = HouseCatalog("R" ,123 ,530045, "Vizag", 2, 200)
    y.add_house()
    y.houses_cost_atmost(price)
    z = HouseCatalog("Re" ,123 ,530045, "Vizag", 2, 200)
    z.add_house()
    z.houses_cost_atmost(price)
    for i in l:
        print(i.house.obj_addr.street, sep =',')
    # print(m)
    print("Street with atmost price are : ", end=" ")

    for i in m:
        print(i.obj_addr.street ,end=" ")

