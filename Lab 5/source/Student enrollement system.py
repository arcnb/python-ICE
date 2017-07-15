import numpy as np

# client class which takes the user information
class clieent(object):
    def __init__(self):
        self._FN =''
        self._LN = ''
    def _intialtxt(self):
        if(self._FN!='' and self._LN!=''):
            print("\nGood_Morning",self._FN,"welcme to student enrollement system!\n")
            print("Student Information:")
            print("Student_Name:", self._FN,self._LN)
        else:
            print("\nNo information available\n")

# System class to show univeristy information
class System():
    def __init__(self):
        self._sys = ''
    def showSystem(self):
        if(self._sys!=''):
            print("System Information:",self._sys,"\n")
        else:
            print("\nNo information available\n")

# user class inheriting Person and address class and displaying details
class Stu(clieent, System):
    def __init__(self, stu_fn, stu_ln, system):
        self.type = "user"
        clieent._FN = stu_fn
        clieent._LN = stu_ln
        clieent._intialtxt(self)
        System._addr = system
        System.showSystem(self)
        # super(User, self).__init__()
        # Person._welcomeMessage(self)

# admin class inheriting Person and address class and displaying details
class Addmin(clieent):
    # constructor
    def __init__(self, stu_fn, stu_ln):
        self.type = "Addmin"
        clieent._FN = stu_fn
        clieent._LastName = stu_ln
        clieent._intialtxt(self)
    def _intialtxt(self):
        super(Addmin, self)._intialtxt()
        print("\nAddmin Signin\n")

# product class displays list of products and if admin gives privileges to edit the items
class Department(object):
    def __init__(self):
        print("Departments you belong to:")
        list = ["Id", "Dep Name", "cgpa"]
        rcount = [1, 2, 3]
        self.data = np.array([[1, 'ece', 3.5],
                         [2, 'cse', 4.0],
                         [3, 'mec', 3.75]])

        row_format = "{:>15}" * (len(list) + 1)
        print(row_format.format("", *list))
        for team, row in zip(rcount, self.data):
            print(row_format.format(team, *row))

    # editing items of list
    def changeList(self, type):
        if(type == "Addmin"):
            print("\nselect the department\n")
            decision = input("please change the department:")
            list = ["Id", "Dep Name", "cgpa"]
            rcount = [1, 2, 3]
            if(decision.upper() == "YES"):
                list = input("Enter your Details(id,name, cgpa):").split(",")
                np.append(self.data, list)
                print(np.append(self.data, list))
        else:
            print("You can enroll only if you belong to above departments!")

# Item details that a user is going to add to cart
class Item(object):
    # constructor
    def __init__(self, unq_id, name, cgpa, q):
        self.id = unq_id
        self.name = name
        self.cgpa = cgpa
        self.q = q

# Cart class that adds the items to user list and calculates the total amount
class Cart(object):
    # constructor
    def __init__(self, user_fn, data):
        self.details = dict()
        self.q = 0
        self.total = 0
        self.__data = data
        print("Hello", user_fn)
        self.itemNum = input("Please pick a dep from the list(Item Id):")

    def pickItem(self, itemnum):
        self.itemNum = itemnum
        for i in range(0, len(self.__data)):
            if (str(self.__data[i][0]) == str(self.itemNum)):
                print("You have picked-", self.__data[i][1])
                c = input("Please input the cgpa:")
                item = Item(self.__data[i][0], self.__data[i][1], self.__data[i][2], c)
                self.add(item)
                print("Your enrollment details" % (int(self.q), int(self.total)))

    def add(self,_item1):
        self.qty = _item1.qty
        self.total = int(_item1.price) * int(_item1.qty)


print("Welcome to students enrollement system")
print("please enter your details.")
us_fn = input("please enter your first name")
us_ln = input("please enter your last name")
address = input("please enter your address")

# Creating instance of user class and accessing various features
us = clieent(us_fn, us_ln, System)
# creating instance of product to get list of items available
Depa = Department()
# creating instance of cart to add items to cart
cart = Cart(us_fn, Depa.data)
cart.pickItem(cart.itemNum)
# accessing change list method to show just admin has access to edit items
Depa.changeList(us.type)



print("----Admin------")
print("please enter your credentials(Admin).")
admin_fn = input("please enter your first name")
admin_ln = input("please enter your last name")

Addmin = clieent(admin_fn, admin_ln)
Addmin._intialtxt()

Depa = Department()

Depa.changeList(Addmin.type)