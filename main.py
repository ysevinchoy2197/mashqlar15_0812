#3-misol
class Phone:
    def __init__(self, model, battarry, imei):
        self.model = model
        self._battary = battarry
        self.__imei = imei

    def call(self, minutes):
        self._battary -= minutes

    def charge(self, x):
        self.__imei = x

    def info(self):
        return f"{self._battary} Grade:{self._battary}"

p1 = Phone("Samsung", "90%", 20)
p1.info()

p1._battary(50)
p1.check_balance()

acc.withdraw(1111, 50)

acc.withdraw(1234, 50)
acc.check_balance()
