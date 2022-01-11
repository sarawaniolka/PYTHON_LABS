
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
                print("The charge of {} has been made. Your account balance is {}.".format(amount,self._balance))
            else:
                print("The funds are insufficient. You currently have {}.".format(self._balance))
        else:
            print("The charge needs to be a positive number.")

    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
            print("You have made a deposit = {}. Your account balance is {}.".format(amount, self._balance))
        else:
            print("You can't deposit a negative number!")

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
        #DO - create a new account and add it to the list of accounts
        # if is_savings:
        #     a = SavingsAccount(customer)
        # else:
        #     a = CheckingAccount(customer)
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        self.acc_list.append(a)
        return a

    def transfer(self, from_account_id, to_account_id, amount):
        #DO - please note that you might need to find the "from" and "to" accounts in the list
        fromid = [x for x in self.cust_list if x.id == from_account_id]
        toid = [x for x in self.cust_list if x.id == to_account_id]
        if len(fromid) == 1:
            if len(toid) == 1:
                print("ok")

            else:
                print("The receiver of the transfer does not exist.")
        else:
            print("The transferor does not exist.")

        # based on the ids provided as input

    def __repr__(self):
        return 'Bank\n{}\n{}'.format(self.cust_list, self.acc_list)

b = Bank()

c1 = b.new_customer('John', 'Brown', 'john@brown.com')
c2 = b.new_customer('Anna', 'Smith', 'anne@smith.com')
c3 = b.new_customer('Sara', 'Waniolka', 'sw116322@student.sgh.waw.pl')

a1 = b.new_account(c1, is_savings=True)
a2 = b.new_account(c1, is_savings=False)
a3 = b.new_account(c3, is_savings=True)



