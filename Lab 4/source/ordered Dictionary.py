# To convert a Dictionary(Usually do not have an order) into an Ordered Dictionary
# we import COLLECTIONS pacakge to use ORDEREDDICT method
#ORDEREDDICT method will sort the key value pairs in increasing order here
import collections
adress=[("Anil","Grades"),
        ("Lab1", 10),
        ("Lab2", 10),
        ("Lab3", 10),
        ("Lab4", 10),
        ("Lab5", 10)]
X=collections.OrderedDict(adress)
print(X)
