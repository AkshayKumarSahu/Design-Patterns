from Adapter.BankAdapter.BankAdapterABC import BankAdapter
from Adapter.Banks.Icicibank import IciciBank


class IciciBankAdapter(BankAdapter):
    def __init__(self):
        self.bank = IciciBank()

    def check_balance(self):
        return self.bank.bal()