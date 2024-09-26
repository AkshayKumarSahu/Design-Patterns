from Observer2.Observer.Observer import Observer


class Swiggy(Observer):
    def update(self,x):
        print("Update Called in Swiggy",x)