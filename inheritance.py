class Phone:
    def call(self):
        print("I am call method from Phone class")

    def message(self):
        print("I am message method from Phone class")


class Samsung(Phone):  # inheritance
    super

    def photo(self):
        print("I am photo method from Sumsung class")


obj = Samsung()
print("Samsung is subclass of Phone class : ", issubclass(Samsung, Phone))
obj.call()
obj.message()
obj.photo()
