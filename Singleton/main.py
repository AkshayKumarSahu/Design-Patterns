class Study:
    def __init__(self):
        self.marks = 0

    def calculate(self):
        print(self.marks)

class Singleton:
    instances = {}                          #Stores the object of the class
    def __new__(cls, *args, **kwargs):
        if cls not in cls.instances:        #Here cls is method parameter and cls.instance is the class variable
            cls.instances[cls] = super().__new__(cls)
        print(cls.instances)
        return cls.instances[cls]


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    study1 = Singleton(Study())
    study2 = Singleton(Study())
    print(s1)
    print(s2)
    print(study2)
    print(study1)