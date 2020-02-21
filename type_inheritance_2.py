print("Multiple inheritance class")


class A:
    def display(self):
        print("I am inside A class")


class B:
    # display1
    def display(self):
        print("I am inside B class")


"""
class C(A,B):
    # A->display
    # B->display
    # def display(self):
    #     print("I am inside C class")
    pass
"""

class C(B,A):
    # A->display
    # B->display
    # def display(self):
    #     print("I am inside C class")
    pass


obj1 = C()
# obj1.display1()
# obj1.display2()
obj1.display()
