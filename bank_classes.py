class BankError(Exception):
    pass


class AccountNotExistsError(BankError):
    pass


class NotEnoughMoneyErrir(BankError):
    pass


class NegativeAmountError(BankError):
    pass


class Customer:
    last_id = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{},{}]'.format(self.id, self.first_name, self.last_name, self.email)


class Account:
    last_id = 0

    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0

    def charge(self, amount):
        if amount<0:
            raise NegativeAmountError('{} amount provided to dpeosit: {}'.format(self.id, amount))
        if amount > self._balance:
            raise NotEnoughMoneyErrir('{} emount provided to deposit: {}'.format(self.id, amount))
        self._balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError('{} amount provided to deposit: {}'.format(self.id, amount))
        self._balance += amount


    def get_balance(self):
        return self._balance

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.last_name, self._balance)


class SavingsAccount(Account):
    interest_rate = 0.02

    def calc_interest(self):
        self._balance += self.interest_rate * self._balance


class CheckingAccount(Account):
    pass


class Bank:
    def __init__(self):
        self.cust_list = []
        self.acc_list = []

    def new_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        self.cust_list.append(c)
        return c

    def new_account(self, customer, is_savings=True):
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        self.acc_list.append(a)
        return a

    def choose_account(self, id):
        return [a for a in self.acc_list if a.id == id]

    def check_transfer(self, from_account, to_account, amount):
        check_transfer = False
        if from_account and to_account:
            if from_account[0].get_balance() >= amount:
                check_transfer = True
        return check_transfer

    def transfer(self, from_account_id, to_account_id, amount):
        from_account = self.acc_list[from_account_id-1]
        to_account = self.acc_list[to_account_id-1]
        from_account.charge(amount)
        to_account.deposit(amount)


    def __repr__(self):
        return 'Bank\n{}\n{}'.format(self.cust_list, self.acc_list)


b = Bank()

c1 = b.new_customer('John', 'Brown', 'john@brown.com')
c2 = b.new_customer('Anna', 'Smith', 'anne@smith.com')
c3 = b.new_customer('Sara', 'Waniolka', 'sw116322@student.sgh.waw.pl')

a1 = b.new_account(c1, is_savings=True)
a2 = b.new_account(c1, is_savings=False)
a3 = b.new_account(c3, is_savings=True)

a1.deposit(100)
print(b)
b.transfer(a1.id, a2.id, 100)
print(b)
