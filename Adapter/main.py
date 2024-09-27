from Adapter.BankAdapter.IciciBankAdapter import IciciBankAdapter
from Adapter.BankAdapter.YesBankAdapter import YesBankAdapter

if __name__ == '__main__':
    bank = IciciBankAdapter()
    # bank = YesBankAdapter()       #Just change the adapter to use different bank i.e client
    print(bank.check_balance())

