import abc


# abstract class Employee
class Employee(metaclass=abc.ABCMeta):
    _firstname = None
    _middlename = None
    _lastname = None
    _fullname = f"{_firstname} {_middlename} {_lastname}"

    @abc.abstractmethod
    def calculate_salary(self):
        pass

    @abc.abstractmethod
    def retrieve_base(self):
        pass

    @abc.abstractmethod
    def get_bonuses(self):
        pass


class ContractEmployee(Employee):
    _base_Country = None

    def __init__(self, value):
        _base_Country = value

    def calculate_salary(self):
        print("Implementation for contract employee")

    @classmethod
    def retrieve_base(cls):
        return cls._base_Country

    @classmethod
    def get_bonuses(cls):
        #    staticmethod
        print("Implementation for contract employee")
