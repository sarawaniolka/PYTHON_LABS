#class -> instances / objects

#DEFINING THE SIMPLEST POSSIBLE CLASS

class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

user1 = User("Joe", "Dough", 43)
user2 = User("Blanca", "Hoolanka", 23)
