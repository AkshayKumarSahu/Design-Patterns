from Observer.Observers.Observer import Observer


class Display(Observer):

    def update(self, temprature, humidity):
        print(f"Temprature : {temprature}, Humidity : {humidity}")