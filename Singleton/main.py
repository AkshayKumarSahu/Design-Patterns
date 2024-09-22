

class Singleton:
    instances = {}                          #Stores the object of the class
    def __new__(cls, *args, **kwargs):
        if cls not in cls.instances:        #Here cls is method parameter and cls.instance is the class variable
            cls.instances[cls] = super().__new__(cls)
        return cls.instances[cls]


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1)
    print(s2)