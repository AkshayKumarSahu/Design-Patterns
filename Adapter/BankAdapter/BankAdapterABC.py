from abc import ABC, abstractmethod


class BankAdapter(ABC):
    @abstractmethod
    def check_balance(self):
        pass
