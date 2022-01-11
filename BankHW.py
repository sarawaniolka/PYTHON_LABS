
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

    #do - add methods "charge" and "deposit" that will change the balance
    def charge(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print("The charge of {} has been made. The account balance of ID:{} is {}.".format(amount, self.id, self._balance))
            else:
                print("The funds are insufficient. You currently have {}.".format(self._balance))
        else:
            print("The charge needs to be a positive number.")

    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
            print("You have made a deposit = {}. The account balance of ID:{} is {}.".format(amount,self.id, self._balance))
        else:
            print("You can't deposit a negative number!")

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
        #DO - create a new customer, add it to a list of customers
        c = Customer(first_name, last_name, email)
        self.cust_list.append(c)
        return c

    def new_account(self, customer, is_savings=True):
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        self.acc_list.append(a)
        return a

    def choose_account(self, id):
        return [a for a in self.acc_list if a.id == id]

    def transfer_allowed(self, from_account, to_account, amount):
        transfer_allowed = False
        if from_account and to_account:
            if from_account[0].get_balance() >= amount:
                transfer_allowed = True
        return transfer_allowed

    def transfer(self, from_account_id, to_account_id, amount):
        from_account, to_account = self.choose_account(from_account_id), self.choose_account(to_account_id)

        if self.transfer_allowed(from_account, to_account, amount):
            to_account[0].deposit(amount)
            from_account[0].charge(amount)
            print("The transfer of {} from ID:{} to ID:{} has been made.".format(amount, from_account_id, to_account_id))
        else:
            print("The transfer cannot be made.")


    def __repr__(self):
        return 'Bank\n{}\n{}'.format(self.cust_list, self.acc_list)

b = Bank()

c1 = b.new_customer('John', 'Brown', 'john@brown.com')
c2 = b.new_customer('Anna', 'Smith', 'anne@smith.com')
c3 = b.new_customer('Sara', 'Waniolka', 'sw116322@student.sgh.waw.pl')

a1 = b.new_account(c1, is_savings=True)
a2 = b.new_account(c1, is_savings=False)
a3 = b.new_account(c3, is_savings=True)


a3.deposit(30)
b.transfer(a3.id,a2.id,20)

