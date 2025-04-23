class SimpleClass:
    pass


class Classey:
    varia=2

    def method(self):
        print(self.varia)

object_one=Classey()
object_Two=Classey()
object_one.varia=3
object_Two.varia=5

# print(object_one.varia)
# print(object_Two.varia)


#class Transport:
    #def __init__(self,air,water):
    #     self.air=air
    #     self.water=water



# obj_transport=Transport("Beluga","Hovercraft")
# obj2=Transport("Jet","Boat")

# print(obj_transport.air,obj_transport.water)
# print(obj2.air,obj2.water)

class Person:
    def __init__(self,fname,lname):
         self.fname=fname
         self.lname=lname

    def printname(self):
        print(self.fname,self.lname)

# x=Person("Michelle","Gakenyi")
# x.printname()
# a=Person("Angella","Wangui")
# a.printname()
# b=Person("Amara","Wacheke")
# b.printname()

class ShoppingCart:
    def __init__(self):
        self.items=[]##created a list
##this method adds item to the list self.items
    def add_item(self,item_name,qty):
        item=(item_name,qty)
        self.items.append(item)

##this method removes item to the list self.items
    def remove_item(self,item_name):
        for item in self.items:
            if item[0]==item_name:
               self.items.remove(item)
               break
##this method calculates how many items there are
    def calculate_total(self):
        total=0
        for item in self.items:
            total+=item[1]
        return total

cart=ShoppingCart()

##adds items to cart
cart.add_item("Kiwi",290)
cart.add_item("Papaya",1000)
cart.add_item("Orange",780)
##displays total items in your cart
print("Current items in Cart")
for item in cart.items:
    print(item[0],"-",item[1])
# displays the total quantity
total_qty=cart.calculate_total()
print("Total Quantity:",total_qty)