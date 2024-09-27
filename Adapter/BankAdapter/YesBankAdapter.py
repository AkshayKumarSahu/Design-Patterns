from Adapter.BankAdapter.BankAdapterABC import BankAdapter
from Adapter.Banks.Yesbank import YesBank


class YesBankAdapter(BankAdapter):

    def __init__(self):
        self.bank = YesBank()

    def check_balance(self):
        return self.bank.balance()
